# Generated by Django 3.2.8 on 2021-12-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='active',
            field=models.IntegerField(default=1),
        ),
    ]
