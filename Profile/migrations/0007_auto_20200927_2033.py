# Generated by Django 3.1.1 on 2020-09-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_no',
            field=models.CharField(default='', max_length=100),
        ),
    ]
