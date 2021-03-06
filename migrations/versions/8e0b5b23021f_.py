"""empty message

Revision ID: 8e0b5b23021f
Revises: f81b763f156d
Create Date: 2020-08-23 16:09:15.761864

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e0b5b23021f'
down_revision = 'f81b763f156d'
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
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bills',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('bill_name', sa.String(length=20), nullable=False),
    sa.Column('bill_due_date', sa.Date(), nullable=True),
    sa.Column('bill_amount', sa.Float(precision=2), nullable=False),
    sa.Column('is_paid', sa.Text(), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paychecks',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pay_date', sa.Date(), nullable=True),
    sa.Column('pay_frequency', sa.Text(), nullable=False),
    sa.Column('filing_status', sa.Text(), nullable=False),
    sa.Column('state', sa.Text(), nullable=False),
    sa.Column('exemptions', sa.Integer(), nullable=False),
    sa.Column('gross_pay', sa.Float(precision=2), nullable=False),
    sa.Column('pre_tax_deductions', sa.Float(precision=2), nullable=True),
    sa.Column('federal_taxes', sa.Float(precision=2), nullable=False),
    sa.Column('state_taxes', sa.Float(precision=2), nullable=False),
    sa.Column('fica_taxes', sa.Float(precision=2), nullable=False),
    sa.Column('total_deductions', sa.Float(precision=2), nullable=False),
    sa.Column('net', sa.Float(precision=2), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings_entries',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('savings_date', sa.Date(), nullable=False),
    sa.Column('transaction_type', sa.String(length=10), nullable=False),
    sa.Column('amount', sa.Float(precision=2), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savings_goals',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('amount', sa.Float(precision=2), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('total_savings_log',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('total', sa.Float(precision=2), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), nullable=True),
    sa.Column('savings_id', postgresql.UUID(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['savings_id'], ['savings_entries.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('total_savings_log')
    op.drop_table('savings_goals')
    op.drop_table('savings_entries')
    op.drop_table('paychecks')
    op.drop_table('bills')
    op.drop_table('users')
    # ### end Alembic commands ###
