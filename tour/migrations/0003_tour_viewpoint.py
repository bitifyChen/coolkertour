# Generated by Django 2.2.13 on 2020-06-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_auto_20200607_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='viewpoint',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='景點'),
        ),
    ]
