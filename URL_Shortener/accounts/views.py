from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CreateUserForm

def logout(request):
    auth_logout(request)
    return redirect(login)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Имя или пароль неверные')
            return render(request, 'accounts/login.html')

    context = {}
    return render(request, 'accounts/login.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        del form.fields['password2']
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт был создан для ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

