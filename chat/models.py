from django.db import models

# Create your models here.

# Model to represent chats
class Chats(models.Model):
    user = models.CharField(max_length=50)  # Field to store the user's name
    chat_box = models.TextField(max_length=500)  # Field to store the chat message

    def __str__(self):
        return f'{self.user} {self.chat_box}'  # String representation of the chat object
