# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.stock'
        db.add_column(u'records_book', 'stock',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.stock'
        db.delete_column(u'records_book', 'stock')


    models = {
        u'records.artist': {
            'Meta': {'object_name': 'Artist'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['records.School']", 'null': 'True', 'blank': 'True'})
        },
        u'records.author': {
            'Meta': {'object_name': 'Author'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'records.book': {
            'Meta': {'object_name': 'Book'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['records.Artist']", 'symmetrical': 'False'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['records.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'publication_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['records.Publisher']"}),
            'stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'records.image': {
            'Meta': {'object_name': 'Image'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['records.Artist']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['records.Book']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'page_no': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'records.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'records.school': {
            'Meta': {'object_name': 'School'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['records']