from django import forms
from django.utils import timezone
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'due_time', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'due_date': 'Optional. Cannot be in the past.',
            'title': 'Required. Max 200 characters.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError("Title is required.")
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date:
            today = timezone.localdate()
            if due_date < today:
                raise forms.ValidationError("The due date cannot be in the past.")
        return due_date

    def clean(self):
        cleaned = super().clean()
        return cleaned