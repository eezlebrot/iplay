from django.conf.urls import url

from . import views

app_name = 'todo'

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^tasklist_update$', views.tasklist_update, name='tasklist_update'),
]