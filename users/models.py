from django.db import models

# Create your models here.
class data(models.Model):
    csv_file=models.FileField(null=True)