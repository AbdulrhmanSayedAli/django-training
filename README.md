# music platform :

## About :

- this is a music platform which contains Artists, Albums and Songs.

- you can create as many artists as you like.
- you can create albums for any artist and upload songs to it (image,audio file).
- you can (as admin) approve any album name if it's name is not explicit.

## Installation :

first install python poetry and learn how to use it with django from [here](https://rasulkireev.com/managing-django-with-poetry/)

after cloning the repository all you have to do is :

- run "poetry install" command
- create a .env file and add your <b>SECRET_KEY<b> to it
- run the django app using the command "poetry run manage.py runserver"

## More :

this project is still in the development phase, all it can do now is :

- create an artist [fields:stage_name,social_link].
- create an album [fields:name,creation_datetime,release_datetime,artist,cost] with at least one song in it.
- create a song [fields:name,image,thumbnsil,album,audio_file].
- create, update and delete those models in the django admin.
- login and logout.
- get all artists with thier albums.
