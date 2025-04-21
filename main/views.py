
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'main/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def menu_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/menu.html')

def market_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/market.html')

def farmers_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/farmers.html')

def nueva_ecija_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/nueva-ecija.html')

def negros_occidental_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/negros-occidental.html')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/profile.html')
