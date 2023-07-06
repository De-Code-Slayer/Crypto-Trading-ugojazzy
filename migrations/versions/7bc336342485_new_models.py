"""new models

Revision ID: 7bc336342485
Revises: bf2a36a3268b
Create Date: 2023-07-06 23:30:47.159018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bc336342485'
down_revision = 'bf2a36a3268b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('trader_profile_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('traded_amount', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('traded_coin', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['trader_profile_id'])
        batch_op.create_foreign_key(None, 'trader_profile', ['trader_profile_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('traded_coin')
        batch_op.drop_column('traded_amount')
        batch_op.drop_column('trader_profile_id')

    # ### end Alembic commands ###