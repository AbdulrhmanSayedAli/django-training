from django.conf import settings
from django.core.mail import send_mail
from musicplatform.celery import app
from artists.models import Artist
from django.utils import timezone
from datetime import timedelta

@app.task
def send_congratulation_email(artist_email, album_name):
    print("started")
    email_from = settings.EMAIL_HOST_USER
    email_to = [artist_email,]
    subject = "Congratulation from our musicplatform"
    body = f"looks like you have created a new album called: {album_name} bravo ya wahsh"
    send_mail( subject, body, email_from, email_to)


@app.task
def check_last_album_30_days():
    email_from = settings.EMAIL_HOST_USER
    subject ="Music Platform Reminder"
    no_albums_body = "Hi {} you have to create an album immediatly there is no time to explain because you still have no albums"
    old_albums_body = "Hi {} you have to create a new album because your inactivity is causing your popularity on our platform to decrease"
    artists = Artist.objects.all().prefetch_related("albums")
    for artist in artists:
        last_album = artist.albums.all().last()
        if not last_album:
            send_mail(subject, no_albums_body.format(artist.stage_name), email_from, [artist.user.email])
        elif last_album.created < timezone.now()-timedelta(days=30):
            send_mail(subject, old_albums_body.format(artist.stage_name), email_from, [artist.user.email])
