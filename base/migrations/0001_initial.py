# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Common'
        db.create_table(u'base_common', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'base', ['Common'])

        # Adding model 'StudentType'
        db.create_table(u'base_studenttype', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['StudentType'])

        # Adding model 'GuideCategory'
        db.create_table(u'base_guidecategory', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['GuideCategory'])

        # Adding model 'Department'
        db.create_table(u'base_department', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['Department'])

        # Adding model 'SocialCategory'
        db.create_table(u'base_socialcategory', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['SocialCategory'])

        # Adding model 'Program'
        db.create_table(u'base_program', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['Program'])

        # Adding model 'Qualification'
        db.create_table(u'base_qualification', (
            (u'common_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['base.Common'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['Qualification'])

        # Adding model 'Contact'
        db.create_table(u'base_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'base', ['Contact'])

        # Adding model 'Guide'
        db.create_table(u'base_guide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Contact'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.GuideCategory'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Department'])),
        ))
        db.send_create_signal(u'base', ['Guide'])

        # Adding model 'Student'
        db.create_table(u'base_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('hall_ticket_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('admn_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('reg_no', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.SocialCategory'])),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sub', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subject', to=orm['base.Department'])),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('guide', self.gf('django.db.models.fields.related.ForeignKey')(related_name='guide', to=orm['base.Guide'])),
            ('co_guide', self.gf('django.db.models.fields.related.ForeignKey')(related_name='co_guide', to=orm['base.Guide'])),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')()),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('present_contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='present_contact', to=orm['base.Contact'])),
            ('original_contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='original_contact', to=orm['base.Contact'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dept_of_spec', to=orm['base.Department'])),
            ('area_of_specialition', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_admission', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('stype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.StudentType'])),
            ('qual1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='qualification_1', to=orm['base.Qualification'])),
            ('qual2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='qualification_2', to=orm['base.Qualification'])),
        ))
        db.send_create_signal(u'base', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Common'
        db.delete_table(u'base_common')

        # Deleting model 'StudentType'
        db.delete_table(u'base_studenttype')

        # Deleting model 'GuideCategory'
        db.delete_table(u'base_guidecategory')

        # Deleting model 'Department'
        db.delete_table(u'base_department')

        # Deleting model 'SocialCategory'
        db.delete_table(u'base_socialcategory')

        # Deleting model 'Program'
        db.delete_table(u'base_program')

        # Deleting model 'Qualification'
        db.delete_table(u'base_qualification')

        # Deleting model 'Contact'
        db.delete_table(u'base_contact')

        # Deleting model 'Guide'
        db.delete_table(u'base_guide')

        # Deleting model 'Student'
        db.delete_table(u'base_student')


    models = {
        u'base.common': {
            'Meta': {'object_name': 'Common'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'base.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'base.department': {
            'Meta': {'object_name': 'Department', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.guide': {
            'Meta': {'object_name': 'Guide'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.GuideCategory']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Contact']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'base.guidecategory': {
            'Meta': {'object_name': 'GuideCategory', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.program': {
            'Meta': {'object_name': 'Program', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.qualification': {
            'Meta': {'object_name': 'Qualification', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.socialcategory': {
            'Meta': {'object_name': 'SocialCategory', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.student': {
            'Meta': {'object_name': 'Student'},
            'admn_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'area_of_specialition': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.SocialCategory']"}),
            'co_guide': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'co_guide'", 'to': u"orm['base.Guide']"}),
            'date_of_admission': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dept_of_spec'", 'to': u"orm['base.Department']"}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'guide': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guide'", 'to': u"orm['base.Guide']"}),
            'hall_ticket_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'original_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'original_contact'", 'to': u"orm['base.Contact']"}),
            'present_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'present_contact'", 'to': u"orm['base.Contact']"}),
            'qual1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qualification_1'", 'to': u"orm['base.Qualification']"}),
            'qual2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qualification_2'", 'to': u"orm['base.Qualification']"}),
            'reg_no': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'stype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.StudentType']"}),
            'sub': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subject'", 'to': u"orm['base.Department']"})
        },
        u'base.studenttype': {
            'Meta': {'object_name': 'StudentType', '_ormbases': [u'base.Common']},
            u'common_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Common']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['base']