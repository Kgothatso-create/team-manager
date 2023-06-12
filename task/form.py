from django import forms
from .models import Task
from datetime import date

class AddtaskForm(forms.ModelForm):
    employeeid = forms.IntegerField(required=True)
    employeename = forms.CharField(max_length=50, required=True)
    dategiven = forms.DateField(required=True, initial=date.today, widget=forms.DateInput(attrs={'readonly': 'readonly'}))
    submissiondate = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'yyyy/mm/dd'}))
    tasktitle = forms.CharField(max_length=100, required=True)
    taskinfo = forms.CharField(widget=forms.TextInput(attrs={'maxlength': 500, 'required': True}))

    class Meta:
        model = Task
        fields = ['employeeid', 'employeename', 'dategiven', 'submissiondate', 'tasktitle', 'taskinfo']
