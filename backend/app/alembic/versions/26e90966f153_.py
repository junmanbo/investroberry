"""empty message

Revision ID: 26e90966f153
Revises: 0cf800006d86
Create Date: 2023-07-20 16:07:22.627147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26e90966f153'
down_revision = '0cf800006d86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('simple_transaction_exchange_id_fkey', 'simple_transaction', type_='foreignkey')
    op.drop_column('simple_transaction', 'exchange_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('simple_transaction', sa.Column('exchange_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('simple_transaction_exchange_id_fkey', 'simple_transaction', 'exchange', ['exchange_id'], ['id'])
    # ### end Alembic commands ###
