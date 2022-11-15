# Generated by Django 4.0.8 on 2022-11-07 12:56

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Text', required=True))])), ('richtext', streams.blocks.RichTextBlock())], blank=True, null=True, use_json_field=None),
        ),
    ]