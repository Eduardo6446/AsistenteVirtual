from django.db import models

# Create your models here.

class Message(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input[:50]