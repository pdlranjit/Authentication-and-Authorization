from django.shortcuts import render,redirect

# Create your views here.
from.models import Task

# def BookList(request):
#     Book.objects.create(name='Ranjit Damase',author='Virat kholi',price=2000.345,published_date='2025-06-23')
#     Book.objects.create(name='Ram',author='hari',price=2123.4567,published_date='2023-1-23')

#     #retrive_book=Book.objects.all()
#     # retrive_book=Book.objects.filter(author='hari')
#     # retrive_book=Book.objects.get(id=1)
#     retrive_book=Book.objects.all()

#     return render(request,"firstapp/login.html",{'book_list':retrive_book})

def tasklist(request):
    if request.method=='GET':
        tasks=Task.objects.all().order_by('-updated')
        return render(request,"firstapp/index.html",{'tasks':tasks})
    
    if request.method=='POST':
        tasks=Task.objects.create(
            body=request.POST.get('body')
        )
       
        return redirect('name_tasks')
def Taskdetail(request,pk):
    if request.method=='GET':
        task =Task.objects.get(id=pk)
        return render(request,'firstapp/detail.html',{'task':task})
    
    if request.method=="POST":
        task=Task.objects.get(id=pk)
        task.body=request.POST.get('body')
        task.save()
        
        return redirect('task_detail',pk=task.id)

def TaskDelete(request,pk):
    task = Task.objects.get(id=pk)

    if request.method=='POST':
        task.delete()
        return redirect('name_tasks')
    
    return render(request,'firstapp/delete.html',{'task':task})
