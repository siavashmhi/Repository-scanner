"""Add repositories table.

Revision ID: 87fd501ee392
Revises: 
Create Date: 2024-08-10 17:30:04.330018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87fd501ee392'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repositories',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('owner', sa.String(length=256), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('last_update_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('repositories', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_repositories_owner'), ['owner'], unique=False)
        batch_op.create_index(batch_op.f('ix_repositories_url'), ['url'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('repositories', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_repositories_url'))
        batch_op.drop_index(batch_op.f('ix_repositories_owner'))

    op.drop_table('repositories')
    # ### end Alembic commands ###
