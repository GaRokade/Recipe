# Generated by Django 5.0.6 on 2024-07-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
