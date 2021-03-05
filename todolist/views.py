from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def home(request):
    context=Todo.objects.all()
    return render(request,'base.html',{'data':context})


def addToDo(request):
  
   item=request.POST['item']
   cost=request.POST['cost']
   datetime=request.POST['datetime']
   profit=request.POST['profit']

   
   new_item=Todo(item=item,cost=cost,datetime=datetime,profit=profit)
   new_item.save()
   


   return redirect('/')

def deleteToDo(request,todo_id):
    del_todo=Todo.objects.get(id=todo_id)
   

    del_todo.delete()
    return redirect('/')

    







