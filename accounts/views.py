from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        role = request.POST.get("role", "customer")

        # Validation
        if not username or not email or not password:
            return render(request, "register.html", {"error": "All fields are required."})

        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match."})

        if len(password) < 6:
            return render(request, "register.html", {"error": "Password must be at least 6 characters."})

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken."})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already registered."})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
        )
        user.save()

        login(request, user)  # auto-login after register
        return redirect("home")

    return render(request, "register.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")  # already logged in, skip login page

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            return render(request, "login.html", {"error": "Please enter username and password."})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the page they were trying to visit (if any)
            next_url = request.GET.get("next", "home")
            return redirect(next_url)
        else:
            return render(request, "login.html", {"error": "Invalid username or password."})

    return render(request, "login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})