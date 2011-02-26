# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Game'
        db.create_table('gameviewer_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_played', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('gameviewer', ['Game'])

        # Adding model 'Rating'
        db.create_table('gameviewer_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gameviewer.Game'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gameviewer', ['Rating'])


    def backwards(self, orm):
        
        # Deleting model 'Game'
        db.delete_table('gameviewer_game')

        # Deleting model 'Rating'
        db.delete_table('gameviewer_rating')


    models = {
        'gameviewer.game': {
            'Meta': {'object_name': 'Game'},
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
