from django.shortcuts import render, redirect
from .models import TodoTask
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.
def Home(request) :
    todo_items = TodoTask.objects.order_by('id')

    form    = TodoListForm()

    context = {'Todo_items' : todo_items,
               'form'      : form}

    return render(request,'TodoList/home.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = TodoTask(text = request.POST['text'])
        new_todo.save()
    return redirect('Home')


def completedTodo(request, todo_id):
    todo = TodoTask.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()
    return redirect('Home')

def deleteCompleted(request):
    todo = TodoTask.objects.filter(completed__exact = True).delete()

    return redirect('Home')

def deleteAll(request):
    todo = TodoTask.objects.all().delete()

    return redirect('Home')
