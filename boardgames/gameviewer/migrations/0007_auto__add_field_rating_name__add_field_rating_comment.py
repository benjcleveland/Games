# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Rating.name'
        db.add_column('gameviewer_rating', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Rating.comment'
        db.add_column('gameviewer_rating', 'comment', self.gf('django.db.models.fields.CharField')(default='', max_length=144), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Rating.name'
        db.delete_column('gameviewer_rating', 'name')

        # Deleting field 'Rating.comment'
        db.delete_column('gameviewer_rating', 'comment')


    models = {
        'gameviewer.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_played': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gameviewer.rating': {
            'Meta': {'object_name': 'Rating'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '144'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameviewer.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['gameviewer']
