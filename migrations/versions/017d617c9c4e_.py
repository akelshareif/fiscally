"""empty message

Revision ID: 017d617c9c4e
Revises: 072139cf913e
Create Date: 2020-08-13 19:38:24.271064

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '017d617c9c4e'
down_revision = '072139cf913e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paychecks',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('pay_date', sa.Date(), nullable=False),
    sa.Column('gross', sa.Float(precision=2), nullable=False),
    sa.Column('net', sa.Float(precision=2), nullable=False),
    sa.Column('user_email', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_email'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('paychecks')
    # ### end Alembic commands ###
