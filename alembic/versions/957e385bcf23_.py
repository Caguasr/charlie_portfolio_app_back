"""empty message

Revision ID: 957e385bcf23
Revises: 030d12125553
Create Date: 2024-03-19 11:53:12.329070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '957e385bcf23'
down_revision: Union[str, None] = '030d12125553'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_information', sa.Column('name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users_information', 'name')
    # ### end Alembic commands ###
