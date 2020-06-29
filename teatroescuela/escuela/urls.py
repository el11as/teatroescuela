from django.conf.urls import url

from . import views

app_name = 'escuela'

urlpatterns = [
    url('registrar/', views.registrar, name='registrar'),

]
