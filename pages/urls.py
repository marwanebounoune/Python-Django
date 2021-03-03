from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('form', views.formul, name="form"),
    path('form/clients', views.postClient, name="postClient"),
    path('form/clients/failed', views.failed, name="failed"),
    path('form/clients/succes', views.succes, name="succes")
]