from django.db import models

# Create your models here.
from django.contrib.auth.models import User


GENDER = ((0,'Male'),(1,'Female'))
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    contact = models.CharField(max_length =10, null=True, blank=True)
    gender = models.IntegerField(default=0,choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
