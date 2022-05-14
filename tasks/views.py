from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
import json

from .models import Task
from .forms import TaskForm

# Create your views here.

def View1(request):
    form = TaskForm()
    context = {
        'form' : form,
    }
    return render(request, 'base.html', context)

def RetrieveAllTasksView(request):
    obj = Task.objects.all().values()
    obj_json = json.dumps(list(obj))
    return JsonResponse({'data':obj_json}, status=200)


def MarkAsComplete(request, id):
    obj = Task.objects.get(id=id)
    obj.completed = not obj.completed
    obj.save()
    return JsonResponse({'obj':model_to_dict(obj)}, status=200)

def NewTaskView(request):
    if request.method == 'POST':
        obj = Task(title=request.POST['title'], description=request.POST['description'])
        obj.save()
        return JsonResponse({'obj':model_to_dict(obj)}, status=200)

def DeleteTask(request, id):
    obj = Task.objects.get(id=id)
    obj_dict = model_to_dict(obj);
    obj.delete()
    return JsonResponse({'obj':obj_dict}, status=200)