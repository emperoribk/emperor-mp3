# Generated by Django 2.2 on 2021-03-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('artiste', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='img')),
                ('song', models.FileField(upload_to='song')),
            ],
        ),
    ]
