# Generated by Django 3.1.2 on 2020-11-03 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_id',
            new_name='id',
        ),
    ]
