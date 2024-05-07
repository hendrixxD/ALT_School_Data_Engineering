"""add data to account

Revision ID: 8e92ce14b6b2
Revises: 66a93b6d4d90
Create Date: 2024-03-09 08:44:59.534394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e92ce14b6b2'
down_revision: Union[str, None] = '66a93b6d4d90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO public.account (id, name, description, last_transaction_date)
        VALUES (1,'Lenge Hendrixx', 'Data engineering at Altschool', Null ),
               (2,'Lenge D Joshua', 'Data engineering at Altschool', '2024-03-08');
        """
    )

def downgrade() -> None:
    op.execute(
        """
        DELETE FROM public.account;
        """
    )