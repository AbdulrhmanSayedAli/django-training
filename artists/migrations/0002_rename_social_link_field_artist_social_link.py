# Generated by Django 4.1.2 on 2022-10-14 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='social_link_field',
            new_name='social_link',
        ),
    ]
