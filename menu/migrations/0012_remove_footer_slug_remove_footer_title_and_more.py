# Generated by Django 4.0.8 on 2022-12-01 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_footer_slug_footer_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='title',
        ),
        migrations.AddField(
            model_name='footer',
            name='footer_social_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
