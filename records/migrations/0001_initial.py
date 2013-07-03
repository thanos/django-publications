# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table(u'records_publisher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('alt_names', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'records', ['Publisher'])

        # Adding model 'Artist'
        db.create_table(u'records_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('alt_names', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'records', ['Artist'])

        # Adding model 'Author'
        db.create_table(u'records_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('alt_names', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'records', ['Author'])

        # Adding model 'Book'
        db.create_table(u'records_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('images', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'records', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name(u'records_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'records.book'], null=False)),
            ('author', models.ForeignKey(orm[u'records.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding M2M table for field artists on 'Book'
        m2m_table_name = db.shorten_name(u'records_book_artists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'records.book'], null=False)),
            ('artist', models.ForeignKey(orm[u'records.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'artist_id'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table(u'records_publisher')

        # Deleting model 'Artist'
        db.delete_table(u'records_artist')

        # Deleting model 'Author'
        db.delete_table(u'records_author')

        # Deleting model 'Book'
        db.delete_table(u'records_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name(u'records_book_authors'))

        # Removing M2M table for field artists on 'Book'
        db.delete_table(db.shorten_name(u'records_book_artists'))


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
            'publication_date': ('django.db.models.fields.DateField', [], {}),
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