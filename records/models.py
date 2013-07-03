from django.db import models

import  logging
LOGGER = logging.getLogger(__name__)

from django.conf import settings
from django.db import models

import tagging

class School(models.Model):
    name = models.CharField(max_length=250)
    alt_names = models.TextField(default='')
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=250)
    alt_names = models.TextField(default='')
    def __unicode__(self):
        return self.name



class Artist(models.Model):
    name = models.CharField(max_length=250)
    alt_names = models.TextField(default='')
    school = models.ForeignKey(School, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=250)
    alt_names = models.TextField(default='')
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(default='')
    pdf = models.FileField(upload_to='pdfs', null=True, blank=True)
    authors = models.ManyToManyField(Author, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    publication_year = models.CharField(max_length=4)
    stock = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title

class Image(models.Model):
    artist = models.ForeignKey(Artist, null=True, blank=True)
    book = models.ForeignKey(Book)
    image = models.ImageField(upload_to='images')
    page_no = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return "{}-{}".format(self.book.title,self.page_no)