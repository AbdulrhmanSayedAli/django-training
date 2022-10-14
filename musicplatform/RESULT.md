## Queries I used and their results :

- create some artists :

```python
>>>Artist.objects.create(stage_name="mahmoud")
<Artist: mahmoud>

>>> Artist.objects.create(stage_name="abdulrhman",social_link="https://www.linkedin.com/in/abdulrhman-sayed-ali-48a089193")
<Artist: abdulrhman>
```

- list down all artists :

```python
>>> list(Artist.objects.all())
[<Artist: abdulrhman>, <Artist: mahmoud>]
```

- list down all artists sorted by name :
  <b>note if we used the same previous query it will also work because stage_name is the default ordering in artists table</b>

```python
list(Artist.objects.all().order_by("stage_name"))
[<Artist: abdulrhman>, <Artist: mahmoud>]
```

- list down all artists whose name starts with a :

```python
>>> list(Artist.objects.filter(stage_name__startswith="a"))
[<Artist: abdulrhman>]
```

- in 2 different ways, create some albums and assign them to any artists :

```python

>>> a = Artist.objects.get(pk=1)
>>> b = Artist.objects.get(pk=2)

#first way
>>> Album.objects.create(name="my album",artist=a,release_datetime="2022-11-11 12:00",cost = 100)
<Album: my album>
>>> b.albums.create(release_datetime="2021-12-12 12:00",cost = 1500)
<Album: New Album>

#second way
>>> a.albums.create(name="best album ever",release_datetime="2023-12-12 12:00",cost = 500)
<QuerySet [<Album: my album>]>
```

- get the latest released album :

```python
>>> Album.objects.all().order_by("-release_datetime")[0]
<Album: best album ever>
```

- get all albums released before today :

```python
>> >now =timezone.now()
>>> Album.objects.filter(release_datetime__lt=now)
<QuerySet [<Album: New Album>]>
```

- get all albums released today or before but not after today :

```python
>>> now =timezone.now()
>>> Album.objects.filter(release_datetime__lte=now)
<QuerySet [<Album: New Album>]>
```

- count the total number of albums (hint: count in an optimized manner) :

```python
>>> all_artists = list(Artist.objects.all())
>>> count = 0
>>> for artist in all_artists:
...     count += len(artist.albums.all())
...
>>> count
3
```

- in 2 different ways, for each artist, list down all of his/her albums :

```python
#first way
>>> all_artists = list(Artist.objects.all())
>>> result = {}
>>> for artist in all_artists:
...     result[artist.stage_name] =list( artist.albums.all())
>>> result
{'abdulrhman': [<Album: New Album>], 'mahmoud': [<Album: my album>, <Album: best album ever>]}

#second way
>>> result ={}
>>> all_albums = Album.objects.all()
>>> for album in all_albums:
...      if not album.artist.stage_name in result :
...              result[album.artist.stage_name] = []
...      result[album.artist.stage_name].append(album)
...
>>> result
{'mahmoud': [<Album: my album>, <Album: best album ever>], 'abdulrhman': [<Album: New Album>]}
```

- list down all albums ordered by cost then by name :

```python
>>> list( Album.objects.all().order_by("name").order_by("cost"))
[<Album: my album>, <Album: best album ever>, <Album: New Album>]
```
