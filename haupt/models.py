# ~*~ coding: utf-8 ~*~
from django.db import models

class Post(models.Model):
	name = models.CharField(verbose_name=u'Title',max_length=255,default='title')
	alias = models.CharField(verbose_name=u'Alias',max_length=255,default='alias')
	text = models.TextField(verbose_name=u'Text',default=" ")
	def __unicode__(self):
         return self.name; 