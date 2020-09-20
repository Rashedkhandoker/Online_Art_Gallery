# Generated by Django 3.1.1 on 2020-09-20 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20200919_0105'),
        ('Artwork', '0003_arrange'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artwork.artwork')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.user')),
            ],
            options={
                'unique_together': {('a_id', 'email')},
            },
        ),
    ]
