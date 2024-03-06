"""product

Revision ID: 5c3053cc6fc8
Revises: 3c90e8078fdc
Create Date: 2024-03-06 11:59:08.484348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c3053cc6fc8'
down_revision: Union[str, None] = '3c90e8078fdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
from sqlalchemy import Column, Integer, String, DECIMAL, VARCHAR, ForeignKey, func, TIMESTAMP


def upgrade() -> None:
    op.create_table("product",
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("name", VARCHAR(30), nullable=False),
                    Column("quantity", VARCHAR(255)),
                    Column("Price", DECIMAL),
                    Column("Category_id", Integer,ForeignKey("Category.id")),
                    Column("TimeStamp", TIMESTAMP, server_default=func.now()))


def downgrade() -> None:
    op.drop_table("product")
