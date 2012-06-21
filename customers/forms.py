# -- coding: utf-8 --
from django import forms

from customers.models import Company, Person

class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person