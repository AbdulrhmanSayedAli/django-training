from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from django.core.exceptions import ValidationError
from imagekit.processors import ResizeToFill
from .models_validators import costValidator,audio_file_validator



class Album (TimeStampedModel):
    name = models.CharField(default="New Album" , max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name="albums")
    release_datetime  = models.DateTimeField()
    cost = models.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)
    is_approved = models.BooleanField(default=False,help_text="Approve the album if its name is not explicit")

    def __str__(self):
        return self.name

    class Meta :
        db_table = "albums"


class Song (models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name="songs")
    name = models.CharField(max_length=200 , blank = True)
    image = models.ImageField(upload_to="songs/images")
    thumbnail = ImageSpecField(source='image',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
    audio_file = models.FileField(upload_to="songs/audios",validators=[audio_file_validator])

    def save(self, *args, **kwargs):
        if not self.name:
         self.name = self.album.name
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta :
        db_table = "songs"