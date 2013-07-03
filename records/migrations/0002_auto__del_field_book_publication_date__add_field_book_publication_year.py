# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Book.publication_date'
        db.delete_column(u'records_book', 'publication_date')

        # Adding field 'Book.publication_year'
        db.add_column(u'records_book', 'publication_year',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=4),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Book.publication_date'
        raise RuntimeError("Cannot reverse this migration. 'Book.publication_date' and its values cannot be restored.")
        # Deleting field 'Book.publication_year'
        db.delete_column(u'records_book', 'publication_year')


    models = {
        u'records.artist': {
            'Meta': {'object_name': 'Artist'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
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
            'images': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'publication_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['records.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'records.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'alt_names': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['records']