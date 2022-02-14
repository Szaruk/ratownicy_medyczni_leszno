import email
from pyexpat import model
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                            .filter(status='opublikowane')

class Post(models.Model):
    STATUS_POST = (
        ('robocza', 'Robocza'),
        ('opublikowane', 'Opublikowane'),
    )
    CATEGORIES = (
        ('szkolenia', 'Szkolenia'),
        ('podstawowe', 'Podstawowe'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    text_post = RichTextField(blank='True')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=13,
                              choices=STATUS_POST,
                              default='robocze')
    imagePost = models.ImageField(null=True, blank='True')
    objects = models.Manager()
    published = PublishedManager()
    categories = models.CharField(max_length=11,
                                  choices=CATEGORIES,
                                  default='podstawowe')
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args = [self.publish.year,
                               self.publish.strftime('%m'),
                               self.publish.strftime('%d'),
                               self.slug])

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to= 'image/')

class StatisticsImage(models.Model):
    statisticsImage = models.FileField(upload_to='statistics/')
    statisticsPublished = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.statisticsPublished.strftime("%d-%m-%Y"))

class AboutUs(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank='True')
    photo = models.FileField(upload_to='person/')


class MainInfo(models.Model):
    MainText = models.TextField()

class InfoSectionTitle(models.Model):
    SectionTitle = models.CharField(max_length=255)

class InfoSection(models.Model):
    InfoSection = models.CharField(max_length=255)

    def __str__(self):
        return self.InfoSection

class InfoSectionDetails(models.Model):
    InfoSectionText = models.CharField(max_length=255)
    InfoSection = models.ForeignKey(InfoSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.InfoSectionText