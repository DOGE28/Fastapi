"""add foreign key to post table

Revision ID: ef48bccc304d
Revises: 328a4237c945
Create Date: 2022-04-11 14:35:35.519091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef48bccc304d'
down_revision = '328a4237c945'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', 
    source_table='posts', 
    referent_table='users', 
    local_cols=['owner_id'], 
    remote_cols=['id'], 
    ondelete="CASCADE"
    )
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
