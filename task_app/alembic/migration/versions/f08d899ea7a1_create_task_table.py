"""create task table

Revision ID: f08d899ea7a1
Revises: 
Create Date: 2023-01-07 21:12:31.690383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f08d899ea7a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(30), nullable=False),
        sa.Column('content', sa.String(255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('tasks')
