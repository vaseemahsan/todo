from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .form import todoform
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class listviewtask(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'

class detailviewtask(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class updateviewtask(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class deleteviewtask(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy ('list')

def add(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'index.html',{'task1':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update1.html',{'f':f, 'task':task})