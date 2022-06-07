import email
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.


class Campaign(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title"))
    slug = models.SlugField(blank=True, verbose_name=_("slug"))
    description = models.TextField(verbose_name=_("description"))
    created_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False, verbose_name=_("Updated at"))
    image = CloudinaryField('Image', overwrite=True, format="jpg")

    def __str__(self) -> str:
        return f"title {self.title} | {self.slug}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Subscriber(models.Model):
    email = models.EmailField(verbose_name=_("email"), max_length=254)
    campaign = models.ForeignKey(Campaign, verbose_name=_(
        "Campaign"), on_delete=models.CASCADE)

    def __str__(self):
        return self.email
