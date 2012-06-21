# -- conding: utf-8 --

from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
  data = {}
  context = RequestContext(request)
  return render_to_response('companies/index.html', data, context_instance = context)