
from django.shortcuts import render, redirect
from home.models import Task
from django.utils import timezone

def home(request):
    context = {'success' : False, 'message': "Your task is added to the all Tasks!"}
    if request.method == "POST":
        title = request.POST.get("name")
        task = Task.objects.filter(taskTitle = title)
        # checking for duplicate task!
        if task.exists():
            context = {'success' : False, 'message': "Task exists with the same name!"}
            print("task exits in the database.")
            return render(request, 'index.html', context)
        desc = request.POST.get("desc")
        time = timezone.now()
        task = Task(taskTitle = title, taskDesc = desc, time = time)
        task.save()
        context = {'success': True}
    return render(request, 'index.html', context)
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)

def deleteTask(request):
    data = request.GET.get('data_param')
    task = Task.objects.filter(taskTitle = data)
    task.delete()
    return redirect('/tasks')

def deleteAllTasks(request):
    allTasks = Task.objects.all()
    allTasks.delete()
    return render(request, 'tasks.html')

def updateTask(request):
    taskTitle = request.GET.get('data_param')
    task = Task.objects.get(taskTitle = taskTitle)
    task.update(taskDesc = "this task is updated!")
    return render('/tasks')