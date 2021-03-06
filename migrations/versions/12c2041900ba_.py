"""empty message

Revision ID: 12c2041900ba
Revises: 6c7ea29788a5
Create Date: 2020-08-19 21:16:10.935704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c2041900ba'
down_revision = '6c7ea29788a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savings_entries', sa.Column('created', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('savings_entries', 'created')
    # ### end Alembic commands ###
