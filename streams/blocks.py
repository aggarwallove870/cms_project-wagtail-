from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import PageChooserBlock


  
class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Title")
    text = blocks.TextBlock(required=True,help_text="Text")
    class Meta:
        template ="streams/title_and_text.html"
        icon="edit"
        label= "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template="streams/richtext.html"
        icon="edit"
        label="RichTextBlock"


class CardBlock(blocks.StructBlock):
    title=blocks.CharBlock(required=True,help_text="Add your Title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
    [

        ("Image", ImageChooserBlock(required=True)),
        ("title", blocks.CharBlock(required=True, max_length=40)),
        ("text", blocks.TextBlock(required=True,max_length=50)),
        ("button", blocks.PageChooserBlock(required=False)),
        ("button_url", blocks.URLBlock(required=False)),
    ]
    )
    )

    class Meta:
        template ="streams/card_block.html"
        icon="placeholder"
        label="staff cards"

