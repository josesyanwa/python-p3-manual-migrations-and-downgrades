"""Renaming students to scholars

Revision ID: df3f18b01ee9
Revises: 791279dd0760
Create Date: 2023-12-20 20:10:06.879977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3f18b01ee9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')