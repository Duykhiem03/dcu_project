from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms
from . import models

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        return render(request, 'index.html', {'user_id':user_id})
    return render(request, 'index.html')

# Register user
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('history')
        
    else:
        form = forms.RegisterForm()
    return render(request, 'auth_form.html', {'form': form, 'form_type': 'sign up'})

# Log in user
def user_login(request):
    if request.method == "POST":
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("You Have Been Logged In!"))
                request.session['user_id'] = user.id
                return redirect('history')
            else:
                messages.success(request, ("There was an error, please try again..."))

    else:
        form = forms.LoginForm()
    return render(request, 'auth_form.html', {'form': form, 'form_type': 'sign in'})

# Log out user
def user_logout(request):
    logout(request)
    return redirect('home')


# Order history
@login_required
def history(request):
    user_id = request.session['user_id']
    user = get_object_or_404(User, id=user_id)
    order_history = models.Order.objects.filter(user=user)
    return render(request, 'history.html', {'order_history':order_history, 'first_name': user.first_name})

# Order Pizza
@login_required
def order(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if (form.is_valid()):
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            form.save_m2m()

            return redirect('checkout', order_id=order.id)
    else:
        form = forms.OrderForm()
    return render(request, 'order.html', {'form':form})

# Detail page
@login_required
def checkout(request, order_id):
    order_detail = get_object_or_404(models.Order, id=order_id)
    if request.method == 'POST':
        form = forms.DetailForm(request.POST, instance=order_detail)
        if (form.is_valid()):
            cleaned_data = form.cleaned_data

            order_detail.customer_name = cleaned_data.get('name')
            order_detail.address = cleaned_data.get('address')

            order_detail.save()

            return redirect('summary', order_id=order_id)
    else:
        form = forms.DetailForm(instance=order_detail)
    return render(request, 'auth_form.html', {'form':form, 'form_type': 'checkout'})

# Order summary
@login_required
def order_summary(request, order_id):
    order_detail = get_object_or_404(models.Order, id=order_id)
    toppings = ', '.join([topping.name for topping in order_detail.toppings.all()])
    return render(request, 'order_summary.html', {'order_detail':order_detail, 'toppings': toppings})