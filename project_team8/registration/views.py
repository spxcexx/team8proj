from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_registration(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            try:
                User.objects.create_user(username=username, password=password)
                return redirect('show_login')
            except IntegrityError:
                return render(request, "registration/registration.html", context={"text_error" : "Такий користувач вже існує"})
        else:
            return render(request, "registration/registration.html", context={"text_error" : "Паролі не збігаються"})
    return render(request, 'registration/registration.html')

def show_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("show_main")
        else:
            return render(request, "registration/login.html", context={"text_error" : "Пароль не правильний"})
    return render(request, 'registration/login.html' )

def show_successful_login(request):
    if request.user.is_authenticated:
        return render(request, "main_page/main_page.html")
    else:
        return redirect("login")

def user_logout(request):
    logout(request)
    return redirect ("login")
