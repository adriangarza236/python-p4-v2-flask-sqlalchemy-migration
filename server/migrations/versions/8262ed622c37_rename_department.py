"""rename department

Revision ID: 8262ed622c37
Revises: bc1738e6e827
Create Date: 2025-02-16 19:01:05.761580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8262ed622c37'
down_revision = 'bc1738e6e827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
