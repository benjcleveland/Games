# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Rating.rating'
        db.alter_column('gameviewer_rating', 'rating', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1))

        # Deleting field 'Game.image'
        db.delete_column('gameviewer_game', 'image')

        # Adding field 'Game.year_published'
        db.add_column('gameviewer_game', 'year_published', self.gf('django.db.models.fields.CharField')(default='', max_length=4), keep_default=False)


    def backwards(self, orm):
        
        # Changing field 'Rating.rating'
        db.alter_column('gameviewer_rating', 'rating', self.gf('django.db.models.fields.IntegerField')())

        # Adding field 'Game.image'
        db.add_column('gameviewer_game', 'image', self.gf('django.db.models.fields.files.FileField')(default='', max_length=500), keep_default=False)

        # Deleting field 'Game.year_published'
        db.delete_column('gameviewer_game', 'year_published')


    models = {
        'gameviewer.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'last_played': ('django.db.models.fields.DateTimeField', [], {}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_published': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'gameviewer.rating': {
            'Meta': {'object_name': 'Rating'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '144'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gameviewer.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'})
        }
    }

    complete_apps = ['gameviewer']
