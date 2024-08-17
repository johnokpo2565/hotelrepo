from .test_setup import TestSetup
from rooms.models import Room
from user.models import User
from django.db.utils import IntegrityError
import uuid

class TestModel(TestSetup):
    
    def test_should_create_a_room(self):

        user = User.objects.create(

            first_name="John",
            last_name="James",
            email="john@gmail.com",
            password="1234567",
        )

        room_data = Room.objects.create(
            id=1,
            room_number='2002B',
            category='Deluxe',
            price=123.00,
            user=user,
            occupied_status=False
        )

        self.assertEqual(room_data.room_number, '2002B')
        self.assertEqual(room_data.category, 'Deluxe')
        self.assertEqual(room_data.price, 123.00)
        self.assertEqual(room_data.user, user)
        self.assertEqual(room_data.occupied_status, False)


    def test_string_representation(self):

        user = User.objects.create(

            first_name="John",
            last_name="James",
            email="john@gmail.com",
            password="1234567",
        )


        room_data = Room.objects.create(
            id=1,
            room_number='2002B',
            category='Deluxe',
            price=123.00,
            user=user,
            occupied_status=False
        )

        self.assertEqual(str(room_data), '2002B - Deluxe')


    def test_cannot_create_a_room_without_required_data(self):
        with self.assertRaises(IntegrityError):

            user = User.objects.create(
            first_name="John",
            last_name="James",
            email="john@gmail.com",
            password="1234567",
            )
            
            Room.objects.create(
                id=1,
                room_number=None,
                category='Deluxe',
                price=123.00,
                user=user,
                occupied_status=False
            )

    
    def test_should_create_new_user(self):

        user = User.objects.create(
            first_name="John",
            last_name="James",
            email="john@gmail.com",
            password="1234567",
        )

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "James")
        self.assertEqual(user.email, "john@gmail.com")
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    
    def test_email_uniquiness(self):
       
            User.objects.create(
                first_name = "John",
                last_name = "James",
                email = "jnr11911@gmail.com",
                password="1234567"
            )
             
            with self.assertRaises(IntegrityError):
                User.objects.create(
                first_name = "John",
                last_name = "James",
                email = "jnr11911@gmail.com",
                password="1234567"
            )
                

    def test_first_name_is_empty(self):
            with self.assertRaises(IntegrityError):
                User.objects.create(
                first_name = None,
                last_name = "James",
                email = "jnr11911@gmail.com",
                password="1234567"
            )
                
    
    def test_last_name_is_empty(self):
         with self.assertRaises(IntegrityError):
              User.objects.create(
                first_name = "John",
                last_name = None,
                email = "jnr11911@gmail.com",
                password="1234567"

              )

    def test_email_is_empty(self):
         with self.assertRaises(IntegrityError):

            User.objects.create(
                first_name = "John",
                last_name = "James",
                email = None,
                password="1234567"
              )
    
    def test_user_public_id(self):
         
         user = User.objects.create_user(
              first_name ="John",
              last_name = "Doe",
              email="johndoe@gmail.com",
              password = "12345678",
         )

         self.assertIsInstance(user,object)