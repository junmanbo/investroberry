import ccxt
import mojito
import time

from app.core.celery_app import celery_app
from app import crud, models, schemas
from app.api import deps
from app.trading import upbit, kis


@celery_app.task(acks_late=True)
def place_order(simple_transaction_id) -> str:
    db = next((deps.get_db()))
    st = crud.simple_transaction.get(db, simple_transaction_id)
    exchange = st.ticker.exchange

    # 키 정보 가져오기
    key = crud.exchange_key.get_key_by_owner_exchange(db, owner_id=st.user_id, exchange_id=exchange.id)

    if exchange.exchange_nm == "UPBIT":
        client = upbit.Upbit(key.access_key, key.secret_key)
    elif exchange.exchange_nm == "KIS":
        client = kis.KIS(key.access_key, key.secret_key, key.account)

    order = client.place_order(st)

    st_in = schemas.SimpleTransactionUpdate(uuid = order["id"])
    crud.simple_transaction.update(db=db, db_obj=st, obj_in=st_in)

    while True:
        order_result = client.check_order(st_in.uuid)
        order_result = order_result["info"]
        print(order_result)
        if order_result["state"] == "done":
            st_in.quantity = order_result["executed_volume"]
            st_in.fee = order_result["paid_fee"]
            st_in.is_filled = True
            crud.simple_transaction.update(db=db, db_obj=st, obj_in=st_in)
            return order_result
        elif order_result["state"] == "cancel":
            st = crud.simple_transaction.get(db, simple_transaction_id)
            if st:
                crud.simple_transaction.remove(db=db, id=st.id)
            return order_result

        time.sleep(0.5)
