"""empty message

Revision ID: 22527c758991
Revises: 023f3c26de91
Create Date: 2020-08-17 14:24:13.009571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '22527c758991'
down_revision = '023f3c26de91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bills',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bill_name', sa.String(length=20), nullable=False),
    sa.Column('bill_due_date', sa.Date(), nullable=True),
    sa.Column('bill_amount', sa.Float(precision=2), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paychecks',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pay_date', sa.Date(), nullable=True),
    sa.Column('gross', sa.Float(precision=2), nullable=False),
    sa.Column('net', sa.Float(precision=2), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings_entry',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('savings_date', sa.Date(), nullable=False),
    sa.Column('transaction_type', sa.String(length=10), nullable=False),
    sa.Column('amount', sa.Float(precision=2), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings_goal',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Float(precision=2), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('savings_goal')
    op.drop_table('savings_entry')
    op.drop_table('paychecks')
    op.drop_table('bills')
    op.drop_table('users')
    # ### end Alembic commands ###
