from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AddUserToWaitlist(models.Model):
    user_email = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email