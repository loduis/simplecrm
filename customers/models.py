# -- coding: utf-8 --

from django.db import models
from django.core.urlresolvers import reverse


db = models;

class Company(db.Model):
  name = db.CharField(max_length = 300)
  website = db.URLField(max_length = 200, blank = True)
  app_id = db.IntegerField(blank = True, null = True);
  
  def __unicode__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('company', args = [self.id]);
  
class Person(db.Model):
  first_name = db.CharField(max_length = 255)
  last_name = db.CharField(max_length = 255, blank = True)
  company = db.ForeignKey(Company, blank=True,null=True, related_name='people')
  email = db.EmailField(max_length = 200)
  phone = db.CharField(max_length = 20, blank = True)
  
  def get_absolute_url(self):
    return reverse('person', args = [self.id]);
  
  
  def __unicode__(self):
    return u'%s %s' % (self.first_name, self.last_name)
  
class Note(db.Model):
  body = db.TextField()
  date = db.DateTimeField()
  company = db.ForeignKey(Company)
  person = db.ForeignKey(Person, blank = True)
  
  def __unicode__(self):
    return self.body  