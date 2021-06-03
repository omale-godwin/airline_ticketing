from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Contact(models.Model):

  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name