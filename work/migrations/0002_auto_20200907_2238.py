# Generated by Django 2.2.15 on 2020-09-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='sub_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='副標題'),
        ),
    ]
