# Generated by Django 5.0 on 2023-12-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='task',
            name='isEditing',
            field=models.BooleanField(default=True),
        ),
    ]
