from django.db import models

# Create your models here.
class Chats(models.Model):
    user = models.CharField(max_length=50)
    chat_box = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user} {self.chat_box}'