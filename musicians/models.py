from django.db import models

# Create your models here.
from django.db import models


class Musician(models.Model):
    Musician_id = models.AutoField(primary_key=True, verbose_name="ID музыканта")
    Musician_name = models.CharField(max_length=100, verbose_name="Имя музыканта/название группы")
    Site = models.CharField(max_length=200, verbose_name="Сайт музыканта")

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Song(models.Model):
    Song_id = models.AutoField(primary_key=True, verbose_name="ID песни")
    Musician_key = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name="Исполнитель песни")
    slug = models.SlugField(default=1, verbose_name="ID исполнителя")
    Song_name = models.CharField(max_length=100, verbose_name="Название песни")
    duration = models.CharField(max_length=50, verbose_name="Длительность песни")
    img = models.CharField(max_length=100, verbose_name="Файл обложки")
    lyrics = models.TextField(verbose_name="Текст песни")
    song_link = models.CharField(max_length=200, default='ссылка на mp3', verbose_name="Файл песни")

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
