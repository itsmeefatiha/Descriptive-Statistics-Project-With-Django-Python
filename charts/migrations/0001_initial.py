# Generated by Django 4.1.6 on 2023-04-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv_files/')),
                ('title', models.CharField(max_length=255)),
                ('x_column', models.CharField(max_length=255)),
                ('y_column', models.CharField(max_length=255)),
            ],
        ),
    ]
