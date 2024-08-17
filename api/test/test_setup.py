from rest_framework.test import APITestCase
from django.test import TransactionTestCase
from django.urls import reverse

class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register-list')
        self.login_url = reverse('login-list')
        # self.booking_url = reverse('user-book-room')

        self.user_data = {
            "first_name":"John",
            "last_name":"James",
            "email":"john@gmail.com",
            "password":"1234567",
        }

        self.room_data = {
            "id":1,
            "room_number":"2002B",
            "category":"Deluxe",
            "price":120.00,
            "user":self.user_data,
            "occupied_status":False
        }
        
        return super().setUp()
    

    def tearDown(self):
        return super().tearDown()