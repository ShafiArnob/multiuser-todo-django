# Generated by Django 3.1.2 on 2021-07-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️'), ('2', '2️'), ('3', '3️'), ('4', '4️'), ('5', '5️'), ('6', '6️'), ('7', '7️'), ('8', '8️'), ('9', '9️'), ('10', '10')], max_length=2),
        ),
    ]
