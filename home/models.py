from django.db import models
from wagtail.core.models import Page
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel 
from wagtail.core.fields import RichTextField
from wagtail.admin.panels import PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page): 
    '''Home page for  Models'''
    templates = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )


    def something(self):
        return self.banner_title

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image")
    ]

    class Meta:
        verbose_name="HomePage"