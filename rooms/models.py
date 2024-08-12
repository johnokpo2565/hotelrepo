from django.db import models
from user.models import User
# Create your models here.

class Room(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    room_number = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=255)
    price = models.FloatField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="room")
    occupied_on = models.DateTimeField(auto_now_add=True)
    occupied_status = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.room_number} - {self.category}'
    
    class Meta:
        indexes = [models.Index(fields=['id','price'])]

