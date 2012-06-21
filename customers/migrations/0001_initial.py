# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('customers_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('customer_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('referred_by', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('customers', ['Company'])

        # Adding model 'Person'
        db.create_table('customers_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='people', null=True, to=orm['customers.Company'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('customers', ['Person'])

        # Adding model 'Note'
        db.create_table('customers_note', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Company'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Person'], blank=True)),
        ))
        db.send_create_signal('customers', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('customers_company')

        # Deleting model 'Person'
        db.delete_table('customers_person')

        # Deleting model 'Note'
        db.delete_table('customers_note')


    models = {
        'customers.company': {
            'Meta': {'object_name': 'Company'},
            'customer_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'referred_by': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'customers.note': {
            'Meta': {'object_name': 'Note'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Company']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Person']", 'blank': 'True'})
        },
        'customers.person': {
            'Meta': {'object_name': 'Person'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'to': "orm['customers.Company']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['customers']