from django.shortcuts import render
from .models import TodoTask
# Create your views here.
def Home(request) :
    todo_items = TodoTask.objects.order_by('id')
    context = {'Todo_items' : todo_items}
    return render(request,'TodoList/home.html', context)
