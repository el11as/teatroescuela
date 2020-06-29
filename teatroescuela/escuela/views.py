from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class TeatroEscuela(TemplateView):
    template_name = 'escuela.html'

def registrar(request):
    try:

        status = True
        message = 'Evio de correo'
        error   = 'Envio de correo exitoso'

        contacto = Contacto()
        contacto.nombre   = request.POST.get('fullname')
        contacto.correo   = request.POST.get('email')
        contacto.telefono = request.POST.get('phone')
        contacto.mensaje  = request.POST.get('message')
        contacto.save()

        enviar_mail(
            html = True,
            to_email = ['admision@teatroescuela.cl'],
            subject = 'Nueva Consulta',
            message = 'mail/nuevo-admin.html',
            data = {
                'nombre'   : request.POST.get('fullname'),
                'email'    : request.POST.get('email'),
                'telefono' : request.POST.get('phone'),
                'mensaje'  : request.POST.get('message'),

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
