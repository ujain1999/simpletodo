from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'task_title',
            'task_description',
        ]
        widgets = {
            'task_title':forms.TextInput(attrs={"placeholder":'Title', "style":"width:100%;"}),
            'task_description':forms.Textarea(attrs={"placeholder":"Description","rows":5, "style":"width:100%;height:'fit-content'"})
        }