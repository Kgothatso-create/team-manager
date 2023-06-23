from django.shortcuts import render, redirect
from .form import AddtaskForm
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

# View to display all tasks on the index page
def index(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'task': task})

# View to add a new task
def addtask(request):
    form = AddtaskForm()
    task = Task.objects.all()

    if request.method == 'POST':
        form = AddtaskForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            employeeid = form.cleaned_data['employeeid']
            employeename = form.cleaned_data['employeename']
            dategiven = form.cleaned_data['dategiven']
            submissiondate = form.cleaned_data['submissiondate']
            tasktitle = form.cleaned_data['tasktitle']
            taskinfo = form.cleaned_data['taskinfo']

            # Create a new Task object and save it
            task_object = Task(employeeid=employeeid, employeename=employeename, dategiven=dategiven, submissiondate=submissiondate, tasktitle=tasktitle, taskinfo=taskinfo)
            task_object.save()

            # Display success message
            messages.success(request, "Task added successfully.")
            return redirect('addtask')
    else:
        # Render the form and existing tasks
        return render(request, 'addtask.html', {'form': form, 'task': task})

# View to display details of a specific task
def viewtask(request, tasktitle):
    task = Task.objects.get(tasktitle=tasktitle)
    return render(request, 'viewtask.html', {'task': task})

# View to delete a specific task
def delete(request, tasktitle):
    if request.method == 'POST':
        task = Task.objects.get(tasktitle=tasktitle)
        task.delete()
    
    # Redirect to the index page after deletion
    return HttpResponseRedirect(reverse('index'))
