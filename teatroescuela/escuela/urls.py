from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'escuela'

urlpatterns = [
    path('', views.TeatroEscuela.as_view(), name='teatro_escuela'),
    path('escuela/registrar/', views.ResgitroView.as_view(), name='registrar'),
]

url(r'^aplicado/$', views.aplicado, name='aplicado'),
