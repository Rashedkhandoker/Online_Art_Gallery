# Generated by Django 3.1.1 on 2020-09-28 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Artwork', '0009_auto_20200928_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
