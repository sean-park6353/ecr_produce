"""empty message

Revision ID: 595796cc0bb4
Revises: 2ccf62a93c8e
Create Date: 2023-02-01 00:27:08.123109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '595796cc0bb4'
down_revision = '2ccf62a93c8e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('diary', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'diary', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'diary', type_='foreignkey')
    op.drop_column('diary', 'user_id')
    # ### end Alembic commands ###