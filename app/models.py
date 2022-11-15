from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks

# Create y our models here.

class FlexPage(Page):
    template= "app/flex_page.html"
    content = StreamField(
        [
            ("title_and_text" , blocks.TitleAndTextBlock()),
            ("richtext", blocks.RichTextBlock()),
            ("card",blocks.CardBlock()),
            # ("cta",blocks.CtaBlock()),
        ],
        null=True,
        blank=True
     )
    subtitle= models.CharField(max_length=255, null= True , blank=True)
    content_panels= Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name= "FlexPage"
        verbose_name_plural="Flex Pages"
          
