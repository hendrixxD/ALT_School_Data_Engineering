"""adding new column

Revision ID: 66a93b6d4d90
Revises: 3ff2f88edd9c
Create Date: 2024-03-09 00:06:25.577148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66a93b6d4d90'
down_revision: Union[str, None] = '3ff2f88edd9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'account',
        sa.Column('last_transaction_date', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
