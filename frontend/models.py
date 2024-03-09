
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from tinymce.models import HTMLField
from pilkit.processors import ResizeToFill


class Services(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    title = models.CharField(max_length=100)
    headline = models.BooleanField(default=False)
    content = HTMLField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    cover_picture = models.ImageField(
        _("Thumbnail"), upload_to="post/thumbnail", blank=True, null=True,
    )
    cover_picture_thumbnail = ImageSpecField(source='cover_picture',
                                             processors=[ResizeToFill(900, 631)],
                                             format="JPEG",
                                             options={'quality': 80})
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse('frontend:service_detail', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = "Services"





class Department(models.Model):
    name = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=200, blank=True, null=True, help_text="Name of the flaticon")
    headline = models.BooleanField(default=False)
    cover_picture = models.ImageField(
        _("Thumbnail"), upload_to="department/thumbnail", blank=True, null=True,
    )
    cover_picture_thumbnail = ImageSpecField(source='cover_picture',
                                             processors=[ResizeToFill(900, 631)],
                                             format="JPEG",
                                             options={'quality': 80})
    content = HTMLField(null=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True)
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Absolute URL for Post"""
        return reverse('frontend:department_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Carousel(models.Model):
    title = models.CharField(_('Title'), max_length=500)
    cover_picture = models.ImageField(
        _("Thumbnail"), upload_to="carousel/thumbnail", blank=True, null=True,
    )
    cover_picture_thumbnail = ImageSpecField(source='cover_picture',
                                             processors=[ResizeToFill(1894, 731)],
                                             format="JPEG",
                                             options={'quality': 80})
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
