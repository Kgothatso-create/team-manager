from django import forms
from .models import Task
from datetime import date

# Form for adding a task
class AddtaskForm(forms.ModelForm):
    employeeid = forms.IntegerField(required=True)  # Field for employee ID (required)
    employeename = forms.CharField(max_length=50, required=True)  # Field for employee name (required)
    dategiven = forms.DateField(required=True, initial=date.today, widget=forms.DateInput(attrs={'readonly': 'readonly'}))  # Field for date given (required), with initial value set to current date and readonly attribute
    submissiondate = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'yyyy/mm/dd'}))  # Field for submission date (required), with a placeholder for date format
    tasktitle = forms.CharField(max_length=100, required=True)  # Field for task title (required)
    taskinfo = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 500, 'required': True}))  # Field for task information (required), with a maximum length of 500 characters

    class Meta:
        model = Task  # Model associated with the form
        fields = ['employeeid', 'employeename', 'dategiven', 'submissiondate', 'tasktitle', 'taskinfo']  # Fields to include in the form
