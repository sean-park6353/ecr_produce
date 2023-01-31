"""empty message

Revision ID: 411988c79f6e
Revises: ad429a91f1f4
Create Date: 2023-02-01 07:46:31.940719

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '411988c79f6e'
down_revision = 'ad429a91f1f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('diary', sa.Column('contributer_id', sa.Integer(), nullable=True))
    op.drop_constraint('diary_ibfk_1', 'diary', type_='foreignkey')
    op.create_foreign_key(None, 'diary', 'user', ['contributer_id'], ['id'])
    op.drop_column('diary', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('diary', sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'diary', type_='foreignkey')
    op.create_foreign_key('diary_ibfk_1', 'diary', 'user', ['user_id'], ['id'])
    op.drop_column('diary', 'contributer_id')
    # ### end Alembic commands ###