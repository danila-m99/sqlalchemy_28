"""Modify Order table

Revision ID: f24635b8adcb
Revises: 91fc5d8dfe79
Create Date: 2024-12-26 16:51:28.340587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f24635b8adcb'
down_revision: Union[str, None] = '91fc5d8dfe79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('price', sa.Float(), nullable=True))
    op.drop_column('orders', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('orders', 'price')
    # ### end Alembic commands ###