from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import Task
import json
from django.forms.models import model_to_dict


@login_required(login_url='login')
def HomeView(request):
    tasks = Task.objects.filter(task_user=request.user).filter(active=True).order_by('task_completed','-last_updated_on').values('id','task_title', 'task_description', 'task_completed')
    context = {
        'user_name' : list(User.objects.filter(username=request.user).values('first_name'))[0]['first_name'],
        'tasks' : tasks,
        'form' : TaskForm(),
    }
    return render(request, 'tasks/home.html', context)

@login_required(login_url='login')
def MarkAsCompleteViewAJAX(request):
    if request.method == 'POST':
        obj = Task.objects.get(id=request.POST['task_id'])
        try:
            obj.task_completed = not obj.task_completed
            obj.save()
            obj_json = json.dumps(model_to_dict(obj))
            return JsonResponse(data={"task":obj_json, "status":1})
        except:
            return(JsonResponse(data={"status":0}))

@login_required(login_url='login')
def CreateNewTaskAJAX(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                task_user=request.user,
                task_title=request.POST['task_title'],
                task_description=request.POST['task_description']
            )
            try:
                task.save()
                return JsonResponse({"status":1}) 
            except:
                return JsonResponse({"status":0})

@login_required(login_url='login')
def DeleteTaskAJAX(request):
    if request.method=='POST':
        try:
            task = Task.objects.get(id=request.POST["task_id"])
            task.active=False
            task.save()
            return JsonResponse({"task_id":task.id, "status":1})
        except:
            return JsonResponse({"status":0})

@login_required(login_url='login')
def EditTaskAJAX(request):
    if request.method=='POST':
        try:
            task = Task.objects.get(id=request.POST["task_id"])
            if task.task_user==request.user:
                task.task_title = request.POST['task_title']
                task.task_description = request.POST['task_description']
                task.save()
                return JsonResponse({"status":1, "task":json.dumps(model_to_dict(task))})
            else:
                return JsonResponse({"status":0})        
        except:
            return JsonResponse({"status":0})

        