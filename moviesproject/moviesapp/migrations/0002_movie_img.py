# Generated by Django 4.1.3 on 2022-11-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=5, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
