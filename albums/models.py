from django.db import models
from artists.models import Artist
from django.core.exceptions import ValidationError
# Create your models here.

def costValidator(cost):
    if cost<0:
        raise ValidationError("Cost must be greater than or equal to zero")
    return cost

class Album (models.Model):
    name = models.CharField(default="New Album" , max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name="albums")
    creation_datetime = models.DateTimeField(auto_now_add = True)
    release_datetime  = models.DateTimeField()
    cost = models.DecimalField(validators=[costValidator],decimal_places=5,max_digits=10)

    def __str__(self):
        return self.name

    class Meta :
        db_table = "albums"