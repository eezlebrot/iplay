from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Task

import datetime

# Create your views here.
def index(request):
  all_tasks = Task.objects.all()
  template = loader.get_template('todo/index.html')
  context = {
    'all_tasks' : all_tasks
  }
  return HttpResponse(template.render(context, request))

def tasklist_update(request):
  aDescription = request.POST['description']
  if(aDescription):
    aDueBy = request.POST['due_by']

    if(aDueBy):
      aDueBy = datetime.datetime.strptime(aDueBy, "%m/%d/%Y")
      t = Task(description=aDescription, due_by=aDueBy)
    else:
      t = Task(description=aDescription)

    t.save()

  else:
    try:
      aRemoval = [key for key, value in request.POST.items() if key.startswith('remove')][0].split('_')[1]
      if(aRemoval):
        Task.objects.filter(id=aRemoval).delete()
    except:
      pass

  return HttpResponseRedirect(reverse('todo:index'))