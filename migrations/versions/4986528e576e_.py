"""empty message

Revision ID: 4986528e576e
Revises: None
Create Date: 2016-06-16 13:18:01.131224

"""

# revision identifiers, used by Alembic.
revision = '4986528e576e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('consultations',
    sa.Column('consult_id', sa.Integer(), nullable=False),
    sa.Column('module_code', sa.String(length=8), nullable=True),
    sa.Column('consult_date', sa.Date(), nullable=True),
    sa.Column('start', sa.Time(), nullable=True),
    sa.Column('end', sa.Time(), nullable=True),
    sa.Column('venue', sa.String(length=40), nullable=True),
    sa.Column('num_of_students', sa.Integer(), nullable=True),
    sa.Column('contact_details', sa.String(length=40), nullable=True),
    sa.Column('teacher_id', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('consult_id')
    )
    op.create_table('registrations',
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('consult_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['consult_id'], ['consultations.consult_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registrations')
    op.drop_table('consultations')
    op.drop_table('users')
    ### end Alembic commands ###