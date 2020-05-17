"""empty message

Revision ID: 8b8df0ce5345
Revises: a149291fe53e
Create Date: 2020-04-21 00:59:29.253903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b8df0ce5345'
down_revision = 'a149291fe53e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###