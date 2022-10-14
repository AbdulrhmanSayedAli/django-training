# music platform :

## About :

this is a music platform which contains Artists and Albums (associated with artists) and a django admin panel to control every thing in this platform.

## Installation :

first install python poetry and learn how to use it with django from [here](https://rasulkireev.com/managing-django-with-poetry/)

after cloning the repository all you have to do is :

- run "poetry install" command
- create a .env file and add your <b>SECRET_KEY<b> to it

## More :

this project is still in the development phase , all it can do now is :

- create an artist [fields:stage_name,social_link]
- create an album [fields:name,creation_datetime,release_datetime,artist,cost]
- create , delete and update those models in the django admin
