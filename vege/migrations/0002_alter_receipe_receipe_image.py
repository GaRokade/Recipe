# Generated by Django 5.0.6 on 2024-07-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='receipe/'),
        ),
    ]