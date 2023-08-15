"""empty message

Revision ID: 0cf800006d86
Revises: b6e008bdfd39
Create Date: 2023-07-20 15:59:09.646334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cf800006d86'
down_revision = 'b6e008bdfd39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('simple_transaction', sa.Column('exchange_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'simple_transaction', 'exchange', ['exchange_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'simple_transaction', type_='foreignkey')
    op.drop_column('simple_transaction', 'exchange_id')
    # ### end Alembic commands ###
