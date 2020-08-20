"""empty message

Revision ID: 33c95d2167b1
Revises: 93c237a79bfd
Create Date: 2020-08-19 16:54:40.312784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '33c95d2167b1'
down_revision = '93c237a79bfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savings_goals', sa.Column('current_savings', sa.Float(precision=2), nullable=True))
    op.drop_constraint('savings_goals_savings_total_id_fkey', 'savings_goals', type_='foreignkey')
    op.drop_column('savings_goals', 'savings_total_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savings_goals', sa.Column('savings_total_id', postgresql.UUID(), autoincrement=False, nullable=True))
    op.create_foreign_key('savings_goals_savings_total_id_fkey', 'savings_goals', 'total_savings_log', ['savings_total_id'], ['id'])
    op.drop_column('savings_goals', 'current_savings')
    # ### end Alembic commands ###
