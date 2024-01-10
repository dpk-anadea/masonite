from masonite.tests import TestCase
from app.models.Workspaces import Workspaces


class WorkspacesTest(TestCase):
    def setUp(self):
        super().setUp()

    connection = "testing"

    def test_something(self):
        self.get("/").assertContains("Workspaces")

        Workspaces.create({"name":"first", "description":"first workspace"})
        self.assertTrue(Workspaces.all().count(), 1)