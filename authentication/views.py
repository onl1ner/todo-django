from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todo:home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authentication/login.html', { 'form': form })

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            
            return redirect('todo:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'authentication/registration.html', { 'form': form })