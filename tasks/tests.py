from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='vineet', password='password123')
        login_url = reverse('token_obtain_pair')
        response = self.client.post(login_url, {'username': 'vineet', 'password': 'password123'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_task(self):
        url = reverse('task-list')  # DRF router name pattern
        data = {
            "title": "Write test cases",
            "description": "Add test cases for API",
            "status": "pending",
            "priority": "high"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Write test cases')

    def test_get_tasks(self):
        Task.objects.create(user=self.user, title="Task 1", description="Sample")
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)
