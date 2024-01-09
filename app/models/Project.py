""" Project Model """

from masoniteorm.relationships import has_many
from masoniteorm.models import Model


class Project(Model):
    """Project Model"""
    __fillable__ = ['name', 'workspace_id', 'body']

    @has_many('workspace_id', 'id')
    def workspace(self):
        from app.models.Workspaces import Workspaces
        return Workspaces
