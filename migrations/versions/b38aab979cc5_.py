"""empty message

Revision ID: b38aab979cc5
Revises: 6b103aa45989
Create Date: 2023-05-14 22:36:00.303506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b38aab979cc5'
down_revision = '6b103aa45989'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('sellPoint', sa.String(length=100), nullable=False),
    sa.Column('price', sa.String(length=100), nullable=False),
    sa.Column('cid', sa.String(length=100), nullable=False),
    sa.Column('num', sa.String(length=100), nullable=False),
    sa.Column('barcode', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=False),
    sa.Column('created', sa.String(length=100), nullable=False),
    sa.Column('updated', sa.String(length=100), nullable=False),
    sa.Column('descs', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###
