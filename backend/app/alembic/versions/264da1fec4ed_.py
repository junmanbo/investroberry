"""empty message

Revision ID: 264da1fec4ed
Revises: 
Create Date: 2023-07-18 09:42:16.717933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '264da1fec4ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('asset_nm', sa.String(length=20), nullable=False),
    sa.Column('asset_knm', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('asset_knm'),
    sa.UniqueConstraint('asset_nm')
    )
    op.create_index(op.f('ix_asset_type_id'), 'asset_type', ['id'], unique=False)
    op.create_table('exchange',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exchange_nm', sa.String(length=50), nullable=True),
    sa.Column('exchange_knm', sa.String(length=50), nullable=True),
    sa.Column('open_time', sa.Time(), nullable=False),
    sa.Column('close_time', sa.Time(), nullable=False),
    sa.Column('is_summer', sa.Boolean(), nullable=True),
    sa.Column('min_interval', sa.Integer(), nullable=True),
    sa.Column('min_amount', sa.Integer(), nullable=True),
    sa.Column('min_digit', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exchange_exchange_nm'), 'exchange', ['exchange_nm'], unique=False)
    op.create_index(op.f('ix_exchange_id'), 'exchange', ['id'], unique=False)
    op.create_table('order_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_type_nm', sa.String(length=20), nullable=False),
    sa.Column('order_type_knm', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_type_knm'),
    sa.UniqueConstraint('order_type_nm')
    )
    op.create_index(op.f('ix_order_type_id'), 'order_type', ['id'], unique=False)
    op.create_table('strategy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strategy_nm', sa.String(length=20), nullable=False),
    sa.Column('strategy_knm', sa.String(length=20), nullable=False),
    sa.Column('strategy_desc', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('strategy_knm'),
    sa.UniqueConstraint('strategy_nm')
    )
    op.create_index(op.f('ix_strategy_id'), 'strategy', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_vip', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('exchange_key',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exchange_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('access_key', sa.String(length=255), nullable=False),
    sa.Column('secret_key', sa.String(length=255), nullable=False),
    sa.Column('account', sa.String(length=20), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['exchange_id'], ['exchange.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_exchange_key_id'), 'exchange_key', ['id'], unique=False)
    op.create_table('ticker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exchange_id', sa.Integer(), nullable=True),
    sa.Column('asset_type_id', sa.Integer(), nullable=True),
    sa.Column('symbol', sa.String(length=50), nullable=False),
    sa.Column('currency', sa.String(length=50), nullable=False),
    sa.Column('ticker_knm', sa.String(length=50), nullable=True),
    sa.Column('marketcap', sa.Integer(), nullable=True),
    sa.Column('maker_fee', sa.Float(), nullable=True),
    sa.Column('taker_fee', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['asset_type_id'], ['asset_type.id'], ),
    sa.ForeignKeyConstraint(['exchange_id'], ['exchange.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('symbol')
    )
    op.create_index(op.f('ix_ticker_id'), 'ticker', ['id'], unique=False)
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ticker_id', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('rebal_period', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_portfolio_id'), 'portfolio', ['id'], unique=False)
    op.create_table('simple_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('ticker_id', sa.Integer(), nullable=True),
    sa.Column('order_type_id', sa.Integer(), nullable=True),
    sa.Column('side', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.Column('is_fiiled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_type_id'], ['order_type.id'], ),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_simple_transaction_id'), 'simple_transaction', ['id'], unique=False)
    op.create_table('portfolio_memo',
    sa.Column('portfolio_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.PrimaryKeyConstraint('portfolio_id')
    )
    op.create_table('portfolio_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=True),
    sa.Column('strategy_id', sa.Integer(), nullable=True),
    sa.Column('is_running', sa.Boolean(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolio.id'], ),
    sa.ForeignKeyConstraint(['strategy_id'], ['strategy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_portfolio_order_id'), 'portfolio_order', ['id'], unique=False)
    op.create_table('portfolio_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_order_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('ticker_id', sa.Integer(), nullable=True),
    sa.Column('order_type_id', sa.Integer(), nullable=True),
    sa.Column('side', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.Column('is_fiiled', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['order_type_id'], ['order_type.id'], ),
    sa.ForeignKeyConstraint(['portfolio_order_id'], ['portfolio_order.id'], ),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_portfolio_transaction_id'), 'portfolio_transaction', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_portfolio_transaction_id'), table_name='portfolio_transaction')
    op.drop_table('portfolio_transaction')
    op.drop_index(op.f('ix_portfolio_order_id'), table_name='portfolio_order')
    op.drop_table('portfolio_order')
    op.drop_table('portfolio_memo')
    op.drop_index(op.f('ix_simple_transaction_id'), table_name='simple_transaction')
    op.drop_table('simple_transaction')
    op.drop_index(op.f('ix_portfolio_id'), table_name='portfolio')
    op.drop_table('portfolio')
    op.drop_index(op.f('ix_ticker_id'), table_name='ticker')
    op.drop_table('ticker')
    op.drop_index(op.f('ix_exchange_key_id'), table_name='exchange_key')
    op.drop_table('exchange_key')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_strategy_id'), table_name='strategy')
    op.drop_table('strategy')
    op.drop_index(op.f('ix_order_type_id'), table_name='order_type')
    op.drop_table('order_type')
    op.drop_index(op.f('ix_exchange_id'), table_name='exchange')
    op.drop_index(op.f('ix_exchange_exchange_nm'), table_name='exchange')
    op.drop_table('exchange')
    op.drop_index(op.f('ix_asset_type_id'), table_name='asset_type')
    op.drop_table('asset_type')
    # ### end Alembic commands ###
