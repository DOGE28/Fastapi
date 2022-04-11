"""add content column to posts table

Revision ID: 90027928db05
Revises: 163429b5203c
Create Date: 2022-04-11 12:10:35.678772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90027928db05'
down_revision = '163429b5203c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
