# Generated by Django 3.1.1 on 2020-10-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artwork', '0013_auto_20201003_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='art_description',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
