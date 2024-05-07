"""adding more data

Revision ID: b07c05d6da40
Revises: 8e92ce14b6b2
Create Date: 2024-03-09 10:07:56.329801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b07c05d6da40'
down_revision: Union[str, None] = '8e92ce14b6b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO public.account (id, name, description, last_transaction_date)
        VALUES (3,'Lenge Regan', 'Data engineering at Altschool', '2024-03-08 10:12:15' ),
               (4,'Lenge D Kim', 'Data engineering at Altschool', '2024-03-08 10:13:20');
        """
    )


def downgrade() -> None:
    op.execute(
        """DELETE FROM public.account"""
    )
