# Generated by Django 4.2.4 on 2023-08-23 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='task_id',
            field=models.CharField(default='asdfasdf', max_length=200),
            preserve_default=False,
        ),
    ]
