"""empty message

Revision ID: bf3cf2275ff8
Revises: 017d617c9c4e
Create Date: 2020-08-13 22:35:51.670661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bf3cf2275ff8'
down_revision = '017d617c9c4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paychecks', sa.Column('user_id', postgresql.UUID(), nullable=True))
    op.drop_constraint('paychecks_user_email_fkey', 'paychecks', type_='foreignkey')
    op.create_foreign_key(None, 'paychecks', 'users', ['user_id'], ['id'])
    op.drop_column('paychecks', 'user_email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paychecks', sa.Column('user_email', postgresql.UUID(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'paychecks', type_='foreignkey')
    op.create_foreign_key('paychecks_user_email_fkey', 'paychecks', 'users', ['user_email'], ['id'])
    op.drop_column('paychecks', 'user_id')
    # ### end Alembic commands ###
