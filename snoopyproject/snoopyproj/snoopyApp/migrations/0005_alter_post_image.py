# Generated by Django 4.2.6 on 2023-10-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snoopyApp', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
