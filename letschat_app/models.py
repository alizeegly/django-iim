from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Chat(models.Model):
    message = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    username = models.CharField(max_length=200, default="Anonymous")
    
    def __str__(self):
        return self.message