# Generated by Django 4.0.8 on 2022-12-02 11:10

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Text', required=True))])), ('richtext', streams.blocks.RichTextBlock()), ('card', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your Title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True)), ('button', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('fourdiv', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True))])))])), ('footer', wagtail.blocks.StructBlock([('footer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=50, required=True)), ('ul_title', wagtail.blocks.CharBlock(max_length=40, required=True))])))])), ('Button', wagtail.blocks.StructBlock([('button', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), ('button_url', wagtail.blocks.URLBlock(required=False))])))])), ('leaderboardsection', wagtail.blocks.StructBlock([('leaderboardsection', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('leader_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('leader_name', wagtail.blocks.TextBlock(max_length=300, required=True)), ('leader_university_name', wagtail.blocks.TextBlock(max_length=300, required=True)), ('leader_university_address', wagtail.blocks.TextBlock(max_length=300, required=True))])))])), ('testimonialslider', wagtail.blocks.StructBlock([('testimonialslider', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('caption', wagtail.blocks.TextBlock(max_length=300, required=True)), ('username', wagtail.blocks.TextBlock(max_length=300, required=True)), ('proffesion', wagtail.blocks.TextBlock(max_length=300, required=True)), ('rating', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('banner', wagtail.blocks.StructBlock([('banner', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_text_block1', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_overlay_text_block2', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_overlay_text_block3', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_1', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_url_1', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_2', wagtail.blocks.TextBlock(max_length=100, required=True)), ('banner_button_url_2', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('volunteer', wagtail.blocks.StructBlock([('volunteer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('volunteers', wagtail.blocks.TextBlock(max_length=100, required=True)), ('text', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('divsection', wagtail.blocks.StructBlock([('divsection', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.TextBlock(max_length=100, required=True)), ('subtitle', wagtail.blocks.TextBlock(max_length=100, required=True)), ('divsection_image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('studentandeducator', wagtail.blocks.StructBlock([('studenteducator', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('heading_student', wagtail.blocks.TextBlock(max_length=100, required=True)), ('sub_heading_student', wagtail.blocks.TextBlock(max_length=100, required=True)), ('button_text_student', wagtail.blocks.TextBlock(max_length=100, required=True)), ('heading_educator', wagtail.blocks.TextBlock(max_length=100, required=True)), ('sub_heading_educator', wagtail.blocks.TextBlock(max_length=100, required=True)), ('button_text_educator', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('banner_section_2', wagtail.blocks.StructBlock([('banner_section_2', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('banner_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('banner_overlay_text', wagtail.blocks.TextBlock(max_length=100, required=True))])))])), ('staticform', wagtail.blocks.StructBlock([])), ('four_div_block_2', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('Image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('text', wagtail.blocks.TextBlock(required=True))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
