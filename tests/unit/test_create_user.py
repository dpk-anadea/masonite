from masonite.tests import TestCase, DatabaseTransactions
from app.models.User import User


class CreateUserTest(TestCase, DatabaseTransactions):
    def setUp(self):
        super().setUp()

    connection = "testing"

    def test_create_user(self):
        User.create({"name":"Anzh", "email":"ang20@gmai.com", "password":"Sav123"})
        self.assertTrue(User.all().count(), 1)
