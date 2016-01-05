from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=128)
    website = models.URLField(blank=True)
    address = models.CharField(max_length=128, blank=True)
    
    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'