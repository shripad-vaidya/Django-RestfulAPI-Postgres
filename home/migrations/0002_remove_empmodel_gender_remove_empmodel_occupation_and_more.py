# Generated by Django 4.1.1 on 2022-09-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='empmodel',
            name='occupation',
        ),
        migrations.AddField(
            model_name='empmodel',
            name='mobile',
            field=models.CharField(default=1234567890, max_length=15),
            preserve_default=False,
        ),
    ]
