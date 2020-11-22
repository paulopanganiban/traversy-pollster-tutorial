from django.urls import path

from . import views  # from all import views

# add a namespace using app_name="name of app"

urlpatterns = [
    path('', views.index, name='index'),
]
