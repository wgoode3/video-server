# Generated by Django 2.1.2 on 2018-11-01 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('mal_id', models.IntegerField(blank=True, null=True)),
                ('mal_title', models.CharField(max_length=255)),
                ('anime_type', models.CharField(max_length=255)),
                ('episodes', models.IntegerField(blank=True, null=True)),
                ('mal_url', models.CharField(max_length=255)),
                ('mal_score', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(default='unknown.jpg', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('fansub_group', models.CharField(max_length=255)),
                ('episode_number', models.CharField(max_length=255)),
                ('subtitles', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(default='unknown.jpg', max_length=255)),
                ('crc32_hash', models.CharField(max_length=8)),
                ('filesize', models.IntegerField(blank=True, null=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='video_app.Anime')),
            ],
        ),
    ]
