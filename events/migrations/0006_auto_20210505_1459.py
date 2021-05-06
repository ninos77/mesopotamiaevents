# Generated by Django 3.1.5 on 2021-05-05 12:59

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210505_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=events.models.get_event_image_path, verbose_name='Your Main Image'),
        ),
    ]
