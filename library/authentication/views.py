from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from .forms import RegisterForm, AuthoriseForm, CustomUserForm
from .models import CustomUser
from django.contrib import messages, auth


def register(request, id=0):
    context = {}
    if request.POST:
        if id == 0:
            form = RegisterForm(request.POST)
        else:
            user = CustomUser.get_by_id(id)
            form = RegisterForm(request.POST, instance=user)
            context["data"] = form
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["data"] = form
    else:
        if id == 0:
            form = RegisterForm()
        else:
            if not request.user.is_authenticated:
                messages.info(request, "Log in first!")
                return redirect("authorise")
            if not CustomUser.get_by_email(request.user.email).role == 1:
                messages.info(request, "You don`t have permission!")
                return redirect("home")
            user = CustomUser.get_by_id(id)
            form = RegisterForm(instance=user)
        context["data"] = form
    return render(request, "authentication/register.html", context=context)


def login(request):
    context = {"email": None, "password": None}
    if request.POST:
        form = AuthoriseForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = CustomUser.get_by_email(email)
            if user.check_password(password):
                current_user = authenticate(request, email=email, password=password, role=user.role)
                user.is_active = True
                auth.login(request, current_user)
                return redirect("home")
            else:
                context["data"] = form
                context["password"] = "Incorrect password"
        except ValueError as ve:
            context["email"] = ve
            context["data"] = form
    else:
        form = AuthoriseForm()
        context["data"] = form
    return render(request, "authentication/login.html", context=context)


def log_out(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("home")


def get_all(request):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "user/get_users.html", {"users": CustomUser.get_all()})


def user_info(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "user/get_user_by_id.html", context={"user": CustomUser.get_by_id(id)})


def edit_user(request, user_id):
    error = ""

    if request.method == "POST" and CustomUser.get_by_email(request.user.email).role == 1:
        user = CustomUser.objects.get(pk=user_id)
        user_updated = CustomUserForm(request.POST, instance=user)
        if user_updated.is_valid():
            user_updated.save()
            return redirect("/")
        else:
            error = "Invalid data"

    user = CustomUser.objects.get(pk=user_id)

    data = {
        'form': CustomUserForm(instance=user),
        'error': error
    }
    return render(request, 'user/user_edit.html', data)


def delete_user(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    CustomUser.delete_by_id(id)
    return redirect("get_users")


def home(request):
    return render(request, "home.html")
