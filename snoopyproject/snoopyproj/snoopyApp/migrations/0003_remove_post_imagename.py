# Generated by Django 4.2.6 on 2023-10-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snoopyApp', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imageName',
        ),
    ]