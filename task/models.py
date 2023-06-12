from django.db import models
from datetime import date

# Create your models here.
class Task(models.Model):
    employeeid = models.IntegerField() # Employee ID
    employeename = models.CharField(max_length=50) # employee name
    dategiven = models.DateField(default=date.today) # Date task was given
    submissiondate = models.DateField() # Date to submit task
    tasktitle = models.CharField(max_length=100) # Task title
    taskinfo = models.TextField(max_length=500) # Task information

    def __str__(self):
        return f"{self.employeeid} {self.tasktitle}"