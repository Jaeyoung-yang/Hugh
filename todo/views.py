from django.shortcuts import render, redirect
from .models import Todo
from .forms import AddForm
# Create your views here.
def todo_view(request):
    todos = Todo.objects.all()
    forms = AddForm()
    data = {
        "todos" : todos,
        "forms" : forms,
    }
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "todo_list.html", data)

def inprog_view(request):
    todos = Todo.objects.all()
    forms = AddForm()
    data = {
        "todos" : todos,
        "forms" : forms,
    }
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "in_progress.html", data)

def delete_todo(request, pk):
    target = Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todos")

def done_todo(request, pk):
    target = Todo.objects.get(pk=pk)
    target.is_done = True
    target.save()
    return redirect("todos")

def test_view(request):
        return render(request, "services.html",{})