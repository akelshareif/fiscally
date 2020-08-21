"""empty message

Revision ID: 8e8eb74383a3
Revises: 5f783c12ff94
Create Date: 2020-08-21 14:38:58.321170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8eb74383a3'
down_revision = '5f783c12ff94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paychecks', sa.Column('gross_pay', sa.Float(precision=2), nullable=False))
    op.drop_column('paychecks', 'gross')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('paychecks', sa.Column('gross', sa.REAL(), autoincrement=False, nullable=False))
    op.drop_column('paychecks', 'gross_pay')
    # ### end Alembic commands ###
