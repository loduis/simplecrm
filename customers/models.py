# -- coding: utf-8 --

from django.db import models

class Company(models.Model):
  name = models.CharField(max_length = 300)
  website = models.URLField(max_length = 200, blank = True)
  app_id = models.IntegerField(blank = True, null = True);
  
  def __unicode__(self):
    return self.name
  
class Person(models.Model):
  first_name = models.CharField(max_length = 255)
  last_name = models.CharField(max_length = 255, blank = True)
  company = models.ForeignKey(Company, related_name='employees')
  email = models.EmailField(max_length = 200)
  phone = models.CharField(max_length = 20, blank = True)
  
  def __unicode__(self):
    return u'%s %s' % (self.first_name, self.last_name)
  
  
class Note(models.Model):
  body = models.TextField()
  date = models.DateTimeField()
  company = models.ForeignKey(Company)
  person = models.ForeignKey(Person, blank = True)
  
  def __unicode__(self):
    return self.body  