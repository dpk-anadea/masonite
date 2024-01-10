from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from masonite.views import View
from config.database import DB

from app.models.Project import Project


class ProjectController(Controller):
    def index(self, view: View, request: Request):
        id = request.param('id')
        projects = Project.where('workspace_id', id)
        context = {
            'project': projects
        }
        return view.render("project.index",  context)

    def create(self, view: View, request: Request):
        id = request.param('id')

        return view.render("project.create", {'workspace_id': id})

    def store(self, view: View, response: Response, request: Request):
        id = request.param('id')
        post_data = request.only('name')

        Project.create({'name': post_data['name'], 'workspace_id':id})

        return response.redirect( f'/workspace/{id}')

    def show(self, view: View, request: Request):
        id = request.param('project_id')
        project = Project.find_or_fail(id)

        context = {
            'project': project
        }

        return view.render("project.show", context)

    def edit(self, view: View, request: Request):
        id = request.param('project_id')
        project = Project.find_or_fail(id)

        context = {
            'project': project
        }

        return view.render("project.edit", context)

    def update(self, view: View, response: Response, request: Request):
        id = request.param('project_id')
        project = Project.find_or_fail(id)

        post_data = request.only('name')

        project.update(post_data)

        return response.redirect('/workspace/@id')

    def destroy(self, response: Response, request: Request ):
        id = request.param('project_id')
        project = Project.find_or_fail(id)
        project.delete()
        return response.redirect('/workspace/@id')
