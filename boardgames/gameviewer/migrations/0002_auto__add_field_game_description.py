# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Game.description'
        db.add_column('gameviewer_game', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=400), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Game.description'
        db.delete_column('gameviewer_game', 'description')


    models = {
        'gameviewer.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_played': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gameviewer.rating': {
            'Meta': {'object_name': 'Rating'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameviewer.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['gameviewer']
