from django.shortcuts import render, redirect
from .form import AddtaskForm
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'task': task})

def addtask(request):
    form = AddtaskForm()
    task = Task.objects.all()

    if request.method =='POST':
        form = AddtaskForm(request.POST)
        if form.is_valid():
            employeeid = form.cleaned_data['employeeid']
            employeename = form.cleaned_data['employeename']
            dategiven = form.cleaned_data['dategiven']
            submissiondate = form.cleaned_data['submissiondate']
            tasktitle = form.cleaned_data['tasktitle']
            taskinfo = form.cleaned_data['taskinfo']

            task_object = Task(employeeid=employeeid, employeename=employeename, dategiven=dategiven, submissiondate=submissiondate, tasktitle=tasktitle, taskinfo=taskinfo)
            task_object.save()

            return redirect('addtask')
    else: 
        return render(request, 'addtask.html',{'form': form, 'task':task })
    
def viewtask(request, tasktitle):
    task = Task.objects.get(tasktitle=tasktitle)
    return render(request, 'viewtask.html', {'task': task})

def delete(request, tasktitle):
    if request.method == 'POST':
        task = Task.objects.get(tasktitle=tasktitle)
        task.delete()
    return HttpResponseRedirect(reverse('index'))
