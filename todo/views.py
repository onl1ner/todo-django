from django.shortcuts import render, redirect
from django.contrib.auth import logout

from todo.models import Task

def home(request):
    if request.user.is_authenticated:
        all_tasks = Task.objects.filter(user__exact=request.user.id)
        
        pending_tasks  = [task for task in all_tasks if not task.is_finished]
        finished_tasks = [task for task in all_tasks if task.is_finished]
        
        return render(request, 'todo/index.html', { 'pending_tasks': pending_tasks, 'finished_tasks': finished_tasks })
    
    return redirect('authentication:login')

def creation_form(request):
    user = request.user
    
    task = Task(user=user, task_name=request.POST['task_name'])
    task.save()
        
    return redirect('todo:home')

def finish(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_finished = True
    
    task.save()
    
    return redirect('todo:home')

def clear_list(request):
    Task.objects.all().delete()
    return redirect('todo:home')

def logout_user(request):
    logout(request)
    return redirect('authentication:login')