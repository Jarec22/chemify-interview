from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDoItem
import datetime

def list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo_app/list.html', {'todos':todos})

def detail(request, pk):
    todo = get_object_or_404(ToDoItem, pk=pk)
    return render(request, 'todo_app/detail.html', {'todo':todo})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todo = ToDoItem.objects.create(title=title, description=description)
        return redirect('todo_app:detail', pk=todo.pk)
    return render(request, 'todo_app/create.html')

def update(request, pk):
    todo = get_object_or_404(ToDoItem, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.updated_at = datetime.datetime.now()
        todo.save()
        return redirect('todo_app:detail', pk=todo.pk)
    return render(request, 'todo_app/update.html', {'todo':todo})

def delete(request, pk):
    todo = get_object_or_404(ToDoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_app:list')
    return render(request, 'todo_app/delete.html', {'todo':todo})

def complete(request, pk):
    todo = get_object_or_404(ToDoItem, pk=pk)
    if request.method == 'POST':
        todo.completed = True
        todo.save()
        return redirect('todo_app:detail', pk=todo.pk)
    return render(request, 'todo_app/complete.html', {'todo': todo})