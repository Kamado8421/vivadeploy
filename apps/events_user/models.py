from django.db import models
from django.contrib.auth.models import User

class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    event_date = models.DateField()
    event_time = models.TimeField()
    description = models.CharField(max_length=200)
    email = models.EmailField()
    instagram_handle = models.CharField(max_length=30)
    whatsapp_number = models.CharField(max_length=15)
    event_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s EventUser {self.id}"
