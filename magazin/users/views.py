from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            return redirect('home')
        else:
            message = "Invalid username or password"
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form,'message': message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create(username=username, email=email, phone=phone, password=password)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def profile_view(request):
    user_data = CustomUser.objects.get(username=request.user.username)
    return render(request, 'profile.html', {'user_data': user_data})


def logout_view(request):
    logout(request)
    return redirect('home')