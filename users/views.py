from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_username = User.objects.filter(username=username).first()
        if user_username:
            messages.error(request, 'Bu foydalanuvchi nomi band! Boshqa nom kiriting!')
            return redirect('register')
        user_email = User.objects.filter(email=email).first()
        if user_email:
            messages.error(request, 'Bu email band! Boshqa email kiriting!')
            return redirect('register')
        
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Siz muvaffaqqiyatli ro`yxatdan o`tdingiz!')
        messages.success(request, 'Iltimos, tizimga kirish uchun login qiling!')
        return redirect('login')
        
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Siz muvaffaqqiyatli tizimga kirdingiz!')
            return redirect('home')
        else:
            messages.error(request, 'Foydalanuvchi nomi yoki parol xato!')
        
    return render(request, 'login.html')    
    
def change_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request, 'Siz muvaffaqqiyatli ma`lumotlaringizni o`zgartirdingiz!')
        return redirect('home')
        
    return render(request, 'change_user.html')