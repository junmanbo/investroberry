"""empty message

Revision ID: 141dda0bbc2c
Revises: 65a8684cf235
Create Date: 2023-08-10 15:53:57.779947

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '141dda0bbc2c'
down_revision = '65a8684cf235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ticker_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('order_type', sa.String(length=10), nullable=True),
    sa.Column('side', sa.String(length=10), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('fee', sa.Float(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_id'), 'transaction', ['id'], unique=False)
    op.drop_index('ix_portfolio_transaction_id', table_name='portfolio_transaction')
    op.drop_table('portfolio_transaction')
    op.drop_index('ix_simple_transaction_id', table_name='simple_transaction')
    op.drop_table('simple_transaction')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('simple_transaction',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('uuid', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ticker_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('side', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('fee', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('order_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], name='simple_transaction_ticker_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='simple_transaction_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='simple_transaction_pkey')
    )
    op.create_index('ix_simple_transaction_id', 'simple_transaction', ['id'], unique=False)
    op.create_table('portfolio_transaction',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('side', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('fee', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('is_fiiled', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('order_type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('portfolio_ticker_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['portfolio_ticker_id'], ['portfolio_ticker.id'], name='portfolio_transaction_portfolio_ticker_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='portfolio_transaction_pkey')
    )
    op.create_index('ix_portfolio_transaction_id', 'portfolio_transaction', ['id'], unique=False)
    op.drop_index(op.f('ix_transaction_id'), table_name='transaction')
    op.drop_table('transaction')
    # ### end Alembic commands ###
