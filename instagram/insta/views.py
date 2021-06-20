from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth   import authenticate, login, logout


def login_view(request):
        if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
                if form.is_valid():
                        username = form.cleaned_data.get("username")
                        password = form.cleaned_data.get("password")
                        user = authenticate(request=request, username = usernaem)
                if user is not None:
                        login(request, user)
        
                return redirect("home")
        else:
                form = AuthenticationForm()
                return render(request, 'login.html', {'form':form})

def logout_view(request):
        logout(request)
        return redirect("home")

def register_view(request):
        if request.method == 'POST':
        form = UserCreationForm(request.POST)

        new_user = CustomUser()
        new_user.username = request.POST["userId"]
        new_user.name = request.POST["name"]
        new_user.nickName = request.POST["nickName"]
        new_user.set_password(request.POST["password"])
        new_user.save()
        
        login(request, new_user)
        return render(request, 'signup.html',{'form':form})

# Create your views here.
