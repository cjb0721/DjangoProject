# Generated by Django 2.2 on 2019-04-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookLibrary', '0003_messinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
