"""create posts table

Revision ID: 7decdbbf7e8e
Revises: 
Create Date: 2022-02-15 12:17:55.899016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7decdbbf7e8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
