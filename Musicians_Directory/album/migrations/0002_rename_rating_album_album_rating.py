# Generated by Django 5.0 on 2024-02-12 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='rating',
            new_name='album_rating',
        ),
    ]
