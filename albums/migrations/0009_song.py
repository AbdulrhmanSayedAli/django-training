# Generated by Django 4.1.2 on 2022-10-22 16:09

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_delete_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='songs/images')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='avatars')),
                ('audio_file', models.FileField(upload_to='songs/audios')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
            options={
                'db_table': 'songs',
            },
        ),
    ]