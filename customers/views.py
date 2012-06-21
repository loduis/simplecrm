# -- conding: utf-8 --

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse


from customers.models import Company, Person
from  customers.forms import CompanyForm, PersonForm


def render(template, request, data = {}):
  context = RequestContext(request)
  return render_to_response(template, data, context_instance = context)

def index(request):
  return render('companies/index.html', request)

def companies(request):
  if request.method == 'POST':
    import json
    form = CompanyForm(request.POST or None)
    data = {}
    data['status'] = 'error'
    if form.is_valid():
      company = form.save();
      data['status'] = 'done';
      data['id'] = company.id
    else:
      data['form'] = form.errors;

    return HttpResponse(json.dumps(data), mimetype="application/json");
  else:
    data = {}
    data['active'] = 'companies';
    data['parties'] = Company.objects.all();
    return render('companies/index.html', request, data)

def company_view(request, company_id):
  data = {}
  company = get_object_or_404(Company, id = company_id);
  data['company'] = company;
  data['people'] = company.people.all();
  
  return render('companies/view.html', request, data)  

def company_new(request):
  data = {}
  data['form'] = CompanyForm()
  return render('companies/form.html', request, data)  
  

def people(request):
  data = {}
  data['active'] = 'people';
  data['parties'] = Person.objects.all();
  
  return render('parties.html', request, data)  
  
def new_people(request):
  data = {}
  data['form'] = PersonForm()
  return render('people/form.html', request, data)  
  

def person(request, person_id):

  data = {}
  person = get_object_or_404(Person, id = person_id);
  
  data['person'] = person;
  data['company'] = person.company;
    
  return render('person.html', request, data)
