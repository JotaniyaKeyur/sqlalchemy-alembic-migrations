"""rename column

Revision ID: 115d1ef8cd73
Revises: 29c31a76c6d5
Create Date: 2026-02-23 17:30:41.943129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '115d1ef8cd73'
down_revision: Union[str, Sequence[str], None] = '29c31a76c6d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.alter_column('user', 'username', new_column_name='fullname')

def downgrade():
    op.alter_column('user', 'fullname', new_column_name='username')
