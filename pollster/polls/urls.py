from django.urls import path

from . import views #from all import views

# add a namespace using app_name="name of app"

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),

]
