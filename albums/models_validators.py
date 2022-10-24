from django.core.exceptions import ValidationError
import os

def costValidator(cost):
    if cost<0:
        raise ValidationError("Cost must be greater than or equal to zero")
    return cost




def audio_file_validator(file):
    if not file:
        raise ValidationError("Couldn't read uploaded file")

    if not os.path.splitext(file.name)[1] in [".mp3",".wav"]:
        raise ValidationError("Doesn't have proper extension")

    return file

