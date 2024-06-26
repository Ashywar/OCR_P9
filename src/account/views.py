from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

from account.models import User
from account.forms import SignInForm, SignUpForm


def login_page(request):
    if request.method == 'POST':
        formIn = SignInForm(request.POST or None)

        if formIn.is_valid():
            print("Valid sign in")

            username = formIn.cleaned_data.get('username')
            password = formIn.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/board')

        return redirect('/account/login')

    else:
        formIn = SignInForm()

    user = User()

    return render(request, 'sign_in.html',
                  {'formIn': formIn})


def sign_up_page(request):
    if request.method == 'POST':
        formUp = SignUpForm(request.POST or None)

        if formUp.is_valid():
            print("Valid sign up")
            print(request.POST["username"])
            user = User.objects.create_user(
                request.POST["username"], '', request.POST["password"])
            login(request, user)
            return redirect('/board')

    else:
        formUp = SignUpForm()

    return render(request, 'sign_up.html',
                  {'formUp': formUp})


def logout_user(request):
    print(request)
    logout(request)
    return redirect('/account/login')
