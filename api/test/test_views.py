from .test_setup import TestSetup
from rest_framework import status
from unittest.mock import patch

class TestViews(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        no_data = {
            'password':'',
            'first_name':'',
            'last_name':'',
            }
        res = self.client.post(self.register_url, no_data, format="json")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data.get('password'), None)
        self.assertEqual(res.data['first_name'][0],'This field may not be blank.')
        self.assertEqual(res.data['last_name'][0], 'This field may not be blank.')

    
    def test_user_can_register(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    @patch('api.serializers.userserializer.LoginSerialier')
    def test_user_can_login(self, MockLoginSerialier):

        # Creating a user

        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Attempting to login in the user

        mock_serializer = MockLoginSerialier.return_value
        mock_serializer.is_valid.return_value = True
        mock_serializer.validated_data = {
            'access':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzNTYzNzExLCJpYXQiOjE3MjM1NjE5MTEsImp0aSI6ImQxYTcwYTVkNGE5ZTQwNzBiMTgxM2EyZTU3YzcyNmM1IiwidXNlcl9pZCI6MX0.KAEC8GqGbp7qRglLgRPlDDG2yyK-fjCFSyf2Xws3Nv0',
            'refresh':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMzY0ODMxMSwiaWF0IjoxNzIzNTYxOTExLCJqdGkiOiIxZTYyYzBiOTM5OGE0M2JlYTVmNTQ5NjVmNTZjNWJjNCIsInVzZXJfaWQiOjF9.hBn8KBGCFBfEuQ4V1D_Q4Muau0mNVfeRzax3c0bVJrc'
        }

        validate_data = {
            'email':'john@gmail.com',
            'password':'1234567'
        }

       

        res = self.client.post(self.login_url, validate_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
