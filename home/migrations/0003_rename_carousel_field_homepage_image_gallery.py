# Generated by Django 4.0.8 on 2022-11-29 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_banner_button_first_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='carousel_field',
            new_name='image_gallery',
        ),
    ]
