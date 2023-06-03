from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_my(request):

    if request.method == "POST":
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
    return render(request, "less_page.html")


def exit_my_account(request):

    logout(request)
    return redirect('login')


def my_regis(request):
    if request.method == 'POST':
        user = User(username=request.POST.get('username'),
                    password=request.POST.get('password'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    )
        user.set_password(user.password)
        user.save()
        return redirect('login')

        print(request.POST)
    return render(request, 'regis.html')
