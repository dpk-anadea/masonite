from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from masonite.views import View

from app.models.Workspaces import Workspaces
from app.models.Project import Project


class ProjectController(Controller):
    def index(self, view: View):
        project = Project.all()

        context = {
            'project': project
        }
        return view.render("project.index",  context)

    def create(self, view: View):
        return view.render("project.create")

    def store(self, view: View, response: Response, request: Request):

        post_data = request.only('name', 'workspace_id')

        Project.create(post_data)

        return response.redirect('/project')

    def show(self, view: View, request: Request):
        id = request.param('id')
        project = Project.find_or_fail(id)

        context = {
            'project': project
        }

        return view.render("project.show", context)

    def edit(self, view: View, request: Request):
        id = request.param('id')
        project = Project.find_or_fail(id)

        context = {
            'project': project
        }

        return view.render("project.edit", context)

    def update(self, view: View, response: Response, request: Request):
        id = request.param('id')
        project = Project.find_or_fail(id)

        post_data = request.only('name')

        project.update(post_data)

        return response.redirect('/project')

    def destroy(self, response: Response, request: Request ):
        id = request.param('id')
        project = Project.find_or_fail(id)
        project.delete()
        return response.redirect('/project')
