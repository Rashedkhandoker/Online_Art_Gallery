# Generated by Django 3.1.1 on 2020-10-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0008_submitcompetition'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='images/thumbnail/'),
        ),
    ]
