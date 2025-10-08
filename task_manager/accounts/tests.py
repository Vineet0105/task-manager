from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TaskTestCase(APITestCase):
    def setup(self):
        login_url = reverse('token_obtain_pair')
        self.user  = User.objects.create_user(username='vineet',password='12312')
        response = self.client.post(login_url,{"username":"vineet","password":"12312"},format="json")
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')


