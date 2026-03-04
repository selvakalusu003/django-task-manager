from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from datetime import date

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']

        if due_date < date.today():
            raise forms.ValidationError("Due date cannot be in the past.")

        return due_date