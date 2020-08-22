"""empty message

Revision ID: f1896d92dddc
Revises: bdd283763bd2
Create Date: 2020-08-21 22:08:42.863607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1896d92dddc'
down_revision = 'bdd283763bd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bills', sa.Column('created', sa.Date(), nullable=True))
    op.add_column('paychecks', sa.Column('created', sa.Date(), nullable=True))
    op.add_column('savings_goals', sa.Column('created', sa.Date(), nullable=True))
    op.add_column('total_savings_log', sa.Column('created', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('total_savings_log', 'created')
    op.drop_column('savings_goals', 'created')
    op.drop_column('paychecks', 'created')
    op.drop_column('bills', 'created')
    # ### end Alembic commands ###
