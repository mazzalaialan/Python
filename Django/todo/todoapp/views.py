from django.shortcuts import render, redirect
from .models import TodoModel


# Create your views here.


def todoview(request):
    mytodo = TodoModel.objects.all()
    context = {'mytodos': mytodo}
    return render(request, 'homepage.html', context)


def addtask(request):
    mytask = request.POST['task']
    TodoModel(task=mytask).save()
    return redirect(request.META['HTTP_REFERER'])


def deletetask(request, taskpk):
    TodoModel.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])


def edittask(request,taskpk):
    context = {'todopk': taskpk}
    return render(request, 'edittask.html',context)


def updatetask(request, taskpk):
    usertask = request.POST['task']
    todo = TodoModel.objects.filter(id = taskpk)[0]
    todo.task = usertask
    todo.save()
    return redirect('homepage')