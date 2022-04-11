"""add last few columns to posts table

Revision ID: 77d2031009bd
Revises: ef48bccc304d
Create Date: 2022-04-11 14:41:46.700217

"""
from time import timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d2031009bd'
down_revision = 'ef48bccc304d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published',
         sa.Boolean(), 
         nullable=False, 
         server_default='TRUE')
         )
    op.add_column('posts', sa.Column(
        'created_at', 
        sa.TIMESTAMP(timezone=True), 
        nullable=False, 
        server_default=sa.text('NOW()'))
        )
    
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
