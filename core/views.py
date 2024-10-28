from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def home(request):
    user = request.user
    data = None
    profile = UserProfile.objects.get(user=user)
    if profile.role == 'state_sevakar':
        data = UserProfile.objects.filter(district=profile.district, role='district_sevakar')
    elif profile.role == 'district_sevakar':
        data = UserProfile.objects.filter(district=profile.district, role='bhagat')
    
    return render(request, "home.html", {'profile':profile, 'data':data})

def logout_user(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f"{username} {password}.")
         
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'signin.html')

def register(request):
    states = State.objects.all()
    districts = District.objects.all()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        district_id = request.POST.get('district')
        state_id = request.POST.get('state')
        district = District.objects.get(id=district_id)
        state = State.objects.get(id=state_id)
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        person = UserProfile.objects.create(user=user, phone=phone, district=district, state=state)
        person.save()
        return redirect('signin')
        
    return render(request, 'register.html', {'states': states, 'districts': districts})