# class Publisher(models.Model):
#     name = models.CharField(max_length=250)
#     alt_names = models.TextField(default='')
#     def __unicode__(self):
#         return self.name



# class Artist(models.Model):
#     name = models.CharField(max_length=250)
#     alt_names = models.TextField(default='')
#     def __unicode__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=250)
#     alt_names = models.TextField(default='')
#     def __unicode__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=80)
#     description = models.TextField(default='')
#     pdf = models.FileField(upload_to='pdfs')
#     images = models.ImageField(upload_to='images')
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     artists = models.ManyToManyField(Artist)
#     publication_year = models.CharField(max_length=4)

#     def __unicode__(self):
#         return self.title

import  logging
LOGGER = logging.getLogger(__name__)


from django.contrib import admin
from . import models


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(models.Publisher, PublisherAdmin)



class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(models.Artist, ArtistAdmin)

class ArtistInlineAdmin(admin.TabularInline):
    model = models.Image.artist.through
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(models.Author, AuthorAdmin)

class AuthorInlineAdmin(admin.TabularInline):
    model = models.Book.author.through
    extra = 0

class ImageAdmin(admin.ModelAdmin):
    list_display = ['book', 'artist', 'page_no']
admin.site.register(models.Image, ImageAdmin)

class ImageInlineAdmin(admin.TabularInline):
    model = models.Author
    extra = 0


# class Image(models.Model):
#     artist = models.ForeignKey(Artist)
#     book = models.ForeignKey(Book)
#     image = models.ImageField(upload_to='images')
#     page_no = models.IntegerField(default=0)
#     description = models.TextField(default='')
#     def __unicode__(self):
#         return self.book.name+' page-'+self.page_no


class BookAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = [ArtistInlineAdmin, AuthorInlineAdmin, ImageInlineAdmin]
admin.site.register(models.Book, BookAdmin)