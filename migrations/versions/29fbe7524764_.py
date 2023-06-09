"""empty message

Revision ID: 29fbe7524764
Revises: 2b985afc12ed
Create Date: 2023-05-19 00:03:22.477480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29fbe7524764'
down_revision = '2b985afc12ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_time', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('update_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('update_time')
        batch_op.drop_column('create_time')

    # ### end Alembic commands ###
