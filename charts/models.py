from django.db import models

# Create your models here.
class Chart(models.Model):
    csv_file = models.FileField(upload_to='csv_files/')
    title = models.CharField(max_length=255)
    x_column = models.CharField(max_length=255)
    y_column = models.CharField(max_length=255)
