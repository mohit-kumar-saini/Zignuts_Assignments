from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
from rest_framework import status
import datetime

User = get_user_model()

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.token_url = reverse("token_obtain_pair")
        resp = self.client.post(self.token_url, {"username":"testuser","password":"pass1234"}, format="json")
        self.access = resp.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access}")
        self.list_url = "/api/tasks/"

    def test_create_task_success(self):
        data = {
            "title": "Test Task",
            "description": "Do stuff",
            "due_date": (datetime.date.today() + datetime.timedelta(days=2)).isoformat(),
            "priority": "high",
            "status": "pending"
        }
        res = self.client.post(self.list_url, data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().owner, self.user)

    def test_create_task_past_due_date_fails(self):
        data = {
            "title": "Bad",
            "due_date": (datetime.date.today() - datetime.timedelta(days=1)).isoformat(),
        }
        res = self.client.post(self.list_url, data, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_cannot_create(self):
        self.client.credentials()
        res = self.client.post(self.list_url, {"title":"x"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_and_delete(self):
        task = Task.objects.create(owner=self.user, title="T")
        url = f"/api/tasks/{task.id}/"
        upd = {"title":"Updated", "description":"d", "priority":"low", "status":"completed"}
        res = self.client.put(url, upd, format="json")
        self.assertIn(res.status_code, (status.HTTP_200_OK, status.HTTP_202_ACCEPTED))
        res2 = self.client.delete(url)
        self.assertEqual(res2.status_code, status.HTTP_204_NO_CONTENT)
