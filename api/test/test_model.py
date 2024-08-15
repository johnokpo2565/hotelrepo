from .test_setup import TestSetup
from rooms.models import Room
from user.models import User

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