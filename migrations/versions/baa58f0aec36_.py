"""empty message

Revision ID: baa58f0aec36
Revises: dfd5198f52db
Create Date: 2020-08-23 16:04:45.682879

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'baa58f0aec36'
down_revision = 'dfd5198f52db'
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
    op.create_foreign_key(None, 'bills', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'paychecks', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'savings_entries', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'savings_goals', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'total_savings_log', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'total_savings_log', type_='foreignkey')
    op.drop_constraint(None, 'savings_goals', type_='foreignkey')
    op.drop_constraint(None, 'savings_entries', type_='foreignkey')
    op.drop_constraint(None, 'paychecks', type_='foreignkey')
    op.drop_constraint(None, 'bills', type_='foreignkey')
    op.drop_table('users')
    # ### end Alembic commands ###
