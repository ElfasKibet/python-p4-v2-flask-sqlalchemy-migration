"""add Department

Revision ID: 871b78a06238
Revises: ec4384de6483
Create Date: 2025-06-20 22:16:42.710477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871b78a06238'
down_revision = 'ec4384de6483'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
