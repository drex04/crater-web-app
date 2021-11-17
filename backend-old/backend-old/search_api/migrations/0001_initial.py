# Generated by Django 3.2.9 on 2021-11-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'artist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CraterUsers',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.TextField(unique=True)),
                ('token', models.TextField(blank=True, null=True)),
                ('password_digest', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crater_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dj',
            fields=[
                ('dj_id', models.AutoField(primary_key=True, serialize=False)),
                ('dj_name', models.TextField(unique=True)),
                ('nts_artist_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('episode_id', models.AutoField(primary_key=True, serialize=False)),
                ('episode_name', models.TextField()),
                ('episode_description', models.TextField(blank=True, null=True)),
                ('episode_date', models.TextField(blank=True, null=True)),
                ('episode_url', models.TextField(unique=True)),
                ('episode_platform', models.TextField()),
            ],
            options={
                'db_table': 'episode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EpisodeDj',
            fields=[
                ('episode_dj_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'episode_dj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EpisodeGenre',
            fields=[
                ('episode_genre_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'episode_genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.TextField(unique=True)),
                ('genre_parent_string', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParentGenre',
            fields=[
                ('parent_genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_genre_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'parent_genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('setlist_track_id', models.AutoField(primary_key=True, serialize=False)),
                ('setlist_seq', models.IntegerField()),
            ],
            options={
                'db_table': 'setlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'song',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SongArtist',
            fields=[
                ('song_artist_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'song_artist',
                'managed': False,
            },
        ),
    ]
