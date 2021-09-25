
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('add', views.addTodoItem, name = 'Add'),
    path('completed/<todo_id>', views.completedTodo, name = 'Completed'),
    path('deletecompleted', views.deleteCompleted, name = 'delete'),
    path('deleteall', views.deleteAll, name = 'deleteAll'),


]
