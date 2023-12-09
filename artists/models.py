from django.db import models
from users.models import User
class Artist (models.Model):
    stage_name = models.CharField(unique=True , max_length = 200)
    social_link = models.URLField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.stage_name

    @property
    def approved_albums(self):
        result = 0
        for album in self.albums.all():
            if album.is_approved:
                result+=1
        return result

    class Meta :
        db_table = "artists"
        ordering = ["stage_name"]