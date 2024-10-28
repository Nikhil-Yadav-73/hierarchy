from django.shortcuts import render, redirect
from .models import Bhakt, DistrictSevak, StateSevak
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def home(request):
    user = request.user
    role = "admin"

    if StateSevak.objects.filter(user=user).exists():
        role = "ss"
        person = StateSevak.objects.get(user=user)
        dist_sevaks = DistrictSevak.objects.filter(state=person.state)
        print(person)
        print(dist_sevaks)
    elif DistrictSevak.objects.filter(user=user).exists():
        role = "ds"
        person = DistrictSevak.objects.get(user=user)
        bhakts = Bhakt.objects.filter(district=person.district)
        print(person)
        print(bhakts)
    elif Bhakt.objects.filter(user=user).exists():
        role = "b"
        print("you are a Bhakt")

    print(role)
    return render(request, "home.html", {"role": role})

def signin(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'signin.html')
