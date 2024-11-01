from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
