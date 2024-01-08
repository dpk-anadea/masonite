from masonite.controllers import Controller
from masonite.views import View
from masonite.response import Response
from masonite.request import Request
from app.models.Workspaces import Workspaces


class WorkspacesController(Controller):
    def index(self, view: View):
        workspace = Workspaces.all()

        context = {
            'workspace':workspace
        }
        return view.render("workspace.index",  context)

    def create(self, view: View):
        return view.render("workspace.create")

    def store(self, view: View, response: Response, request: Request):

        post_data = request.only('name', 'description', 'is_active')

        Workspaces.create(post_data)

        return response.redirect('/')

    def show(self, view: View, request: Request):
        id = request.param('id')
        workspace = Workspaces.find_or_fail(id)

        context = {
            'workspace':workspace
        }

        return view.render("workspace.show", context)

    def edit(self, view: View, request: Request):
        id = request.param('id')
        workspace = Workspaces.find_or_fail(id)

        context = {
            'workspace':workspace
        }

        return view.render("workspace.edit", context)

    def update(self, view: View, response: Response, request: Request):
        id = request.param('id')
        workspace = Workspaces.find_or_fail(id)

        post_data = request.only('name', 'description', 'is_active')

        workspace.update(post_data)

        return response.redirect('/')

    def destroy(self, response: Response, request: Request ):
        id = request.param('id')
        workspace = Workspaces.find_or_fail(id)
        workspace.delete()
        return response.redirect('/')
