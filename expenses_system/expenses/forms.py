from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expense, Budget, Schedule, Category, Notification

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(min_length=1)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=1)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, min_length=1)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'period', 'start_date', 'end_date', 'category']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['reminder_type', 'frequency', 'start_date', 'end_date', 'amount', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        # , 'recommended_percentage'

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['notification_type', 'trigger', 'message']