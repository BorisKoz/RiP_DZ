# Generated by Django 3.1.5 on 2021-01-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0003_auto_20210107_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.CharField(default='текст песни', max_length=3000),
        ),
        migrations.AddField(
            model_name='song',
            name='song_link',
            field=models.CharField(default='ссылка на mp3', max_length=200),
        ),
    ]