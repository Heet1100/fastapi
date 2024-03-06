"""Category tale

Revision ID: 3c90e8078fdc
Revises: 
Create Date: 2024-03-06 11:09:50.392618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime, VARCHAR, ForeignKey, func, TIMESTAMP

# revision identifiers, used by Alembic.
revision: str = '3c90e8078fdc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Category",
                    Column("id",Integer,primary_key=True,autoincrement=True),
                    Column("name",VARCHAR(30),nullable=False),
                    Column("description",VARCHAR(255)),
                    Column("TimeStamp",TIMESTAMP,server_default=func.now()))



def downgrade() -> None:
    op.drop_table("Category")
