"""add foreign-key to posts table

Revision ID: 5c55358f598e
Revises: df9c7cd0783f
Create Date: 2022-02-15 15:06:26.864080

"""
from alembic import op
from matplotlib.pyplot import table
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c55358f598e'
down_revision = 'df9c7cd0783f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
