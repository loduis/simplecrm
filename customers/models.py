# -- coding: utf-8 --

from django.db import models
from django.core.urlresolvers import reverse

class Company(models.Model):
  name = models.CharField(max_length = 300)
  website = models.URLField(max_length = 200, blank = True)
  customer_id = models.IntegerField(blank = True, null = True)
  referred_by = models.CharField(max_length = 200, blank = True)
  
  def __unicode__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('company', args = [self.id]);
  
class Person(models.Model):
  first_name = models.CharField(max_length = 255)
  last_name = models.CharField(max_length = 255, blank = True)
  company = models.ForeignKey(Company, blank=True,null=True, related_name='people')
  email = models.EmailField(max_length = 200)
  phone = models.CharField(max_length = 20, blank = True)
  
  def get_absolute_url(self):
    return reverse('person', args = [self.id]);
  
  
  def __unicode__(self):
    return u'%s %s' % (self.first_name, self.last_name)
  
class Note(models.Model):
  body = models.TextField()
  date = models.DateTimeField()
  company = models.ForeignKey(Company)
  person = models.ForeignKey(Person, blank = True)
  
  def __unicode__(self):
    return self.body  