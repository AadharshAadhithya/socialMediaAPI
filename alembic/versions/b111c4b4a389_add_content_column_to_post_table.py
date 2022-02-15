"""add content column to post table

Revision ID: b111c4b4a389
Revises: 7decdbbf7e8e
Create Date: 2022-02-15 12:24:25.393543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b111c4b4a389'
down_revision = '7decdbbf7e8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
