"""Add user table

Revision ID: df9c7cd0783f
Revises: b111c4b4a389
Create Date: 2022-02-15 12:30:02.493872

"""
from http import server
from alembic import op
from pytz import timezone
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df9c7cd0783f'
down_revision = 'b111c4b4a389'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),

                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade():
    op.drop_table('users')
