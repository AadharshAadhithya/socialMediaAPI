"""add last few cols

Revision ID: cf6c4fffabd8
Revises: 5c55358f598e
Create Date: 2022-02-15 15:10:54.208121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf6c4fffabd8'
down_revision = '5c55358f598e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
    ))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
