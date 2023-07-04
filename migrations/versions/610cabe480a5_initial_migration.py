"""Initial migration

Revision ID: 610cabe480a5
Revises: 
Create Date: 2023-07-02 19:21:51.065296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '610cabe480a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('dob', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('country', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('temporary_address', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('permanent_address', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phone', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('ssn', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('display_photo', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('refferals', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('postal_code', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['full_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('postal_code')
        batch_op.drop_column('refferals')
        batch_op.drop_column('display_photo')
        batch_op.drop_column('ssn')
        batch_op.drop_column('phone')
        batch_op.drop_column('permanent_address')
        batch_op.drop_column('temporary_address')
        batch_op.drop_column('country')
        batch_op.drop_column('dob')
        batch_op.drop_column('password')
        batch_op.drop_column('full_name')

    # ### end Alembic commands ###