from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from todo.models import Todo, User


class TodoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass",
        )
        self.token = Token.objects.create(user=self.user)
        self.todo = Todo.objects.create(
            description="Test Todo",
            user=self.user,
        )
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_list_todos(self):
        response = self.client.get("/todo/todos/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_add_todo(self):
        data = {"description": "Test adding todo"}
        response = self.client.post("/todo/add/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_delete_todo(self):
        response = self.client.delete(f"/todo/{self.todo.id}/delete/")
        self.assertEqual(response.status_code, 204)

    def test_mark_todo_completed(self):
        response = self.client.patch(f"/todo/{self.todo.id}/complete/")
        self.assertEqual(response.status_code, 204)
