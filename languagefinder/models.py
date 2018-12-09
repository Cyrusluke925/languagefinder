from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return  self.user.username

class Marker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    title = models.CharField(max_length=40)
    symbol = models.TextField()

    def __str__(self):
        return self.user.username 
