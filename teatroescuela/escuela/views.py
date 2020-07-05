from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from escuela.models import *
from utilidades.views import *

# Create your views here.

class TeatroEscuela(TemplateView):
    template_name = 'escuela.html'


class ResgitroView(View):

    def post(self, request, *args, **kwargs):

        try:
            status = True
            message = 'Evio de correo'
            error   = 'Envio de correo exitoso'

            contacto = Contacto()
            contacto.nombre   = request.POST.get('a-nombre')
            contacto.correo   = request.POST.get('a-email')
            contacto.telefono = request.POST.get('a-phone')
            contacto.mensaje  = request.POST.get('a-mensaje')
            contacto.save()

            enviar_mail(
                html = True,
                to_email = ['admision@teatroescuela.cl'],
                subject = 'Nueva Consulta',
                message = 'mail/nuevo-admin.html',
                data = {
                    'nombre'   : request.POST.get('a-nombre'),
                    'email'    : request.POST.get('a-email'),
                    'telefono' : request.POST.get('a-phone'),
                    'mensaje'  : request.POST.get('a-mensaje'),
                },
            )

            return JsonResponse({
                'status'  : status,
                'message' : message,
                'error'   : error
            })

        except Exception as e:

            return JsonResponse({
                'status'  : status,
                'message' : message,
                'error'   : str(e)
            }, status = 500)

def aplicado(request):
    context = {}
    return render(request, 'aplicado.html', context)

def escuela(request):
    context = {}
    return render(request, 'escuela.html', context)
