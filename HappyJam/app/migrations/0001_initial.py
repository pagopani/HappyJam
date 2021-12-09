# Generated by Django 2.2.24 on 2021-11-30 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Instrument')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Movie')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('instrument_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Instrument')),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='music_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Music'),
        ),
        migrations.AddConstraint(
            model_name='single',
            constraint=models.UniqueConstraint(fields=('uid', 'instrument_id'), name='single_unique'),
        ),
        migrations.AddConstraint(
            model_name='room',
            constraint=models.UniqueConstraint(fields=('id', 'user'), name='room_unique'),
        ),
    ]
