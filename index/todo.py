from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "details", "date"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter title of the task"}),
            "details": forms.Textarea(
                attrs={"placeholder": "Enter description of the task"}
            ),
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
