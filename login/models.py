from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
