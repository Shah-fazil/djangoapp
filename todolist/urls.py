from . import views
from django.urls import path,include

urlpatterns = [path('',views.home,name='home'),
    path('addtodo/',views.addToDo,name='addTodo'),
    path('deletetodo/<int:todo_id>/',views.deleteToDo,name='deleteTodo')
   
]