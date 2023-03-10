"""empty message

Revision ID: 8fdd06a1490a
Revises: 411988c79f6e
Create Date: 2023-02-01 07:47:44.446090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8fdd06a1490a'
down_revision = '411988c79f6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=10), nullable=False),
    sa.Column('contents', sa.Text(length=300), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('contributer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contributer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.drop_index('ix_diary_id', table_name='diary')
    op.drop_table('diary')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diary',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('contents', mysql.TEXT(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('contributer_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['contributer_id'], ['user.id'], name='diary_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_diary_id', 'diary', ['id'], unique=False)
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
