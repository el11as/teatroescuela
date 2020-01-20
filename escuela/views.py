from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class TeatroEscuela(TemplateView):
    print('ACACACAC')
    template_name = 'escuela.html'
