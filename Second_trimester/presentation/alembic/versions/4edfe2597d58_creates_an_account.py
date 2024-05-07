"""creates an account

Revision ID: 4edfe2597d58
Revises: 
Create Date: 2024-03-09 20:01:30.653960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4edfe2597d58'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    	'account',
    	sa.Column('id', sa.Integer, primary_key=True),
    	sa.Column('name', sa.String(50), nullable=False),
    	sa.Column('description', sa.String(200)),
	)



def downgrade() -> None:
    pass
