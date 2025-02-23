from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'email', 'first_name', 'last_name', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class OrderForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=models.PizzaSize.objects.all(), widget=forms.Select(attrs={'class': 'custom-select mb-3', 'placeholder': 'Size'}))
    crust_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Crust type'}))
    sauce = forms.ModelChoiceField(queryset=models.PizzaSauce.objects.all(), widget=forms.Select(attrs={'class': 'custom-select mb-3', 'placeholder': 'Sauce'}))
    cheese = forms.ModelChoiceField(queryset=models.Cheese.objects.all(), widget=forms.Select(attrs={'class': 'custom-select mb-3', 'placeholder': 'Cheese'}))
    toppings = forms.ModelMultipleChoiceField(queryset=models.Toppings.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'placeholder': 'Toppings'}))

    class Meta:
        model = models.Order
        fields = ['size', 'crust_type', 'sauce', 'cheese', 'toppings']

class DetailForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card number'}))
    expired_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'}))
    
    def clean(self):
        expired_date = self.cleaned_data.get('expired_date')
        cvv = self.cleaned_data.get('cvv')
        card_number = self.cleaned_data.get('card_number')
        
        try:
            if (len(cvv) != 3):
                raise forms.ValidationError("Invalid cvv number. Must have 3 digits")
            if (len(card_number) != 16):
                raise forms.ValidationError("Invalid card number. Must have 16 digits")
            cvv = int(cvv)
            card_number = int(card_number)
        except ValueError:
            raise forms.ValidationError("Invalid number. Contain only numbers.")
        
        # Check if the expired date follows MM/YY format
        try:
            month, year = expired_date.split('/')
            if len(month) != 2 or len(year) != 2:
                raise forms.ValidationError("Invalid expiration date format. Use MM/YY.")
            elif int(month) > 12 or int(month) <= 0 or int(year) <= 0:
                raise forms.ValidationError("Invalid expiration date. Use MM/YY.")
        except ValueError:
            raise forms.ValidationError("Invalid expiration date format. Use MM/YY.")
        
        return super().clean()

    class Meta:
        model = models.Order
        fields = ['name', 'address', 'card_number', 'expired_date', 'cvv']