from django.http import HttpResponse, HttpResponseRedirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import render, get_object_or_404, reverse

def TaskListView(request):
    tasks = Task.objects.all()
    total = Task.objects.count()
    completed = Task.objects.filter(completed=True).count()
    pending = total - completed
    context = {
        'tasks': tasks,
        'total': total,
        'completed': completed,
        'pending': pending,
    }
    return render(request, 'task_list.html',context)

def TaskDetailView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task':task})

def TaskCreateView(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def TaskUpdateView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else :
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task})

def TaskDeleteView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect(reverse('task_list'))
    return HttpResponseRedirect('task_detail', pk=pk)

def ToggleTaskCompleteView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse('task_list'))
