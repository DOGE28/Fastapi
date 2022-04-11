"""add user table

Revision ID: 328a4237c945
Revises: 90027928db05
Create Date: 2022-04-11 14:23:13.662203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '328a4237c945'
down_revision = '90027928db05'
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
        sa.UniqueConstraint('email')
    )

    pass


def downgrade():
    pass
