from rest_framework.test import APITestCase
from django.test import TransactionTestCase
from django.urls import reverse

class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register-list')
        self.login_url = reverse('login-list')

        self.user_data = {
            "first_name":"John",
            "last_name":"James",
            "email":"john@gmail.com",
            "password":"1234567",
        }
        
        return super().setUp()
    

    def tearDown(self):
        return super().tearDown()