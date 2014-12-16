# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstagramProfile'
        db.create_table(u'zeropush_pushdevice', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sgauth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal(u'zeropush', ['PushDevice'])

    def backwards(self, orm):
        # Deleting model 'InstagramProfile'
        db.delete_table(u'zeropush_pushdevice')

    complete_apps = ['zeropush']
