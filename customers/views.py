# -- conding: utf-8 --

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


from customers.models import Company, Person


def index(request):
  data = {}
  context = RequestContext(request)
  return render_to_response('companies/index.html', data, context_instance = context)

def companies(request):
  data = {}
  data['active'] = 'companies';
  data['parties'] = Company.objects.all();
  
  context = RequestContext(request)  
  
  return render_to_response('parties.html', data, context_instance = context)

def people(request):
  data = {}
  data['active'] = 'people';
  data['parties'] = Person.objects.all();
  
  context = RequestContext(request)  
  
  return render_to_response('parties.html', data, context_instance = context)


def company(request, company_id):
  data = {}
  company = get_object_or_404(Company, id = company_id);
  
  data['company'] = company;
  data['people'] = company.people.all();
  
  context = RequestContext(request)

  return render_to_response('company.html', data, context_instance = context)

def person(request, person_id):

  data = {}
  person = get_object_or_404(Person, id = person_id);
  
  data['person'] = person;
  data['company'] = person.company;
    
  context = RequestContext(request)

  return render_to_response('person.html', data, context_instance = context)

  