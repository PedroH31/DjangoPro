from django.urls import path

from sitedevpro.turmas import views

app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice'),
]
