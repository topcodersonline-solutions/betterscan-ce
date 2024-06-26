"""
This file is part of Betterscan CE (Community Edition).

Betterscan is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Betterscan is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Betterscan. If not, see <https://www.gnu.org/licenses/>.

Originally licensed under the BSD-3-Clause license with parts changed under
LGPL v2.1 with Commons Clause.
See the original LICENSE file for details.

"""
"""Initial models.

Revision ID: acd2826ea902
Revises: 
Create Date: 2016-11-20 23:05:33.370022

"""

# revision identifiers, used by Alembic.
revision = 'acd2826ea902'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gitrepository',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('public_key', sa.Text(), nullable=True),
    sa.Column('private_key', sa.Text(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('default_branch', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('path_', sa.String(), nullable=True),
    sa.Column('project', sa.String(length=32), nullable=True),
    sa.Column('pk', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['project'], ['project.pk'], name='gitrepository_project_project', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('project', name='unique_gitrepository_project')
    )
    op.create_index(op.f('ix_gitrepository_created_at'), 'gitrepository', ['created_at'], unique=False)
    op.create_index(op.f('ix_gitrepository_default_branch'), 'gitrepository', ['default_branch'], unique=False)
    op.create_index(op.f('ix_gitrepository_path_'), 'gitrepository', ['path_'], unique=False)
    op.create_index(op.f('ix_gitrepository_pk'), 'gitrepository', ['pk'], unique=False)
    op.create_index(op.f('ix_gitrepository_project'), 'gitrepository', ['project'], unique=False)
    op.create_index(op.f('ix_gitrepository_updated_at'), 'gitrepository', ['updated_at'], unique=False)
    op.create_index(op.f('ix_gitrepository_url'), 'gitrepository', ['url'], unique=False)
    op.create_table('gitsnapshot',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('committer_date_ts', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=64), nullable=True),
    sa.Column('log', sa.Text(), nullable=True),
    sa.Column('tree_sha', sa.String(length=40), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('author_name', sa.String(length=100), nullable=True),
    sa.Column('committer_date', sa.DateTime(), nullable=True),
    sa.Column('project', sa.String(length=32), nullable=True),
    sa.Column('sha', sa.String(length=40), nullable=True),
    sa.Column('snapshot', sa.String(length=32), nullable=True),
    sa.Column('author_date_ts', sa.Integer(), nullable=True),
    sa.Column('pk', sa.String(length=32), nullable=False),
    sa.Column('author_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project'], ['project.pk'], name='gitsnapshot_project_project', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['snapshot'], ['snapshot.pk'], name='gitsnapshot_snapshot_snapshot', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('project', 'sha', name='unique_together_gitsnapshot_project_sha'),
    sa.UniqueConstraint('snapshot', name='unique_gitsnapshot_snapshot')
    )
    op.create_index(op.f('ix_gitsnapshot_author_date'), 'gitsnapshot', ['author_date'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_author_date_ts'), 'gitsnapshot', ['author_date_ts'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_committer_date'), 'gitsnapshot', ['committer_date'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_committer_date_ts'), 'gitsnapshot', ['committer_date_ts'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_created_at'), 'gitsnapshot', ['created_at'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_hash'), 'gitsnapshot', ['hash'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_pk'), 'gitsnapshot', ['pk'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_project'), 'gitsnapshot', ['project'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_sha'), 'gitsnapshot', ['sha'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_snapshot'), 'gitsnapshot', ['snapshot'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_tree_sha'), 'gitsnapshot', ['tree_sha'], unique=False)
    op.create_index(op.f('ix_gitsnapshot_updated_at'), 'gitsnapshot', ['updated_at'], unique=False)
    op.create_table('gitbranch',
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('remote', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('project', sa.String(length=32), nullable=True),
    sa.Column('last_analyzed_snapshot', sa.String(length=32), nullable=True),
    sa.Column('pk', sa.String(length=32), nullable=False),
    sa.Column('head_snapshot', sa.String(length=32), nullable=True),
    sa.Column('hash', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['head_snapshot'], ['gitsnapshot.pk'], name='gitbranch_gitsnapshot_head_snapshot', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['last_analyzed_snapshot'], ['gitsnapshot.pk'], name='gitbranch_gitsnapshot_last_analyzed_snapshot', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['project'], ['project.pk'], name='gitbranch_project_project', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('project', 'name', name='unique_together_gitbranch_project_name')
    )
    op.create_index(op.f('ix_gitbranch_created_at'), 'gitbranch', ['created_at'], unique=False)
    op.create_index(op.f('ix_gitbranch_hash'), 'gitbranch', ['hash'], unique=False)
    op.create_index(op.f('ix_gitbranch_head_snapshot'), 'gitbranch', ['head_snapshot'], unique=False)
    op.create_index(op.f('ix_gitbranch_last_analyzed_snapshot'), 'gitbranch', ['last_analyzed_snapshot'], unique=False)
    op.create_index(op.f('ix_gitbranch_name'), 'gitbranch', ['name'], unique=False)
    op.create_index(op.f('ix_gitbranch_pk'), 'gitbranch', ['pk'], unique=False)
    op.create_index(op.f('ix_gitbranch_project'), 'gitbranch', ['project'], unique=False)
    op.create_index(op.f('ix_gitbranch_remote'), 'gitbranch', ['remote'], unique=False)
    op.create_index(op.f('ix_gitbranch_updated_at'), 'gitbranch', ['updated_at'], unique=False)
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_gitbranch_updated_at'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_remote'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_project'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_pk'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_name'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_last_analyzed_snapshot'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_head_snapshot'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_hash'), table_name='gitbranch')
    op.drop_index(op.f('ix_gitbranch_created_at'), table_name='gitbranch')
    op.drop_table('gitbranch')
    op.drop_index(op.f('ix_gitsnapshot_updated_at'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_tree_sha'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_snapshot'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_sha'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_project'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_pk'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_hash'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_created_at'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_committer_date_ts'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_committer_date'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_author_date_ts'), table_name='gitsnapshot')
    op.drop_index(op.f('ix_gitsnapshot_author_date'), table_name='gitsnapshot')
    op.drop_table('gitsnapshot')
    op.drop_index(op.f('ix_gitrepository_url'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_updated_at'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_project'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_pk'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_path_'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_default_branch'), table_name='gitrepository')
    op.drop_index(op.f('ix_gitrepository_created_at'), table_name='gitrepository')
    op.drop_table('gitrepository')
    ### end Alembic commands ###
