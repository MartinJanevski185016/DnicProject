# Generated by Django 4.1 on 2022-08-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_rename_video_youtube_url_remove_youtube_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube',
            name='title',
        ),
    ]
