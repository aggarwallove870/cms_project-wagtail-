# Generated by Django 4.0.8 on 2022-12-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_remove_footer_slug_remove_footer_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='social_media_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link_title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
