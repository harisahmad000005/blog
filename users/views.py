from django.contrib.auth.forms import AuthenticationForm
from django.core.checks.messages import Error
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import *
from django.views.generic import CreateView,FormView
from django.contrib.auth import authenticate , login
from django.contrib import messages



# Create your views here.

def user_home_page(request):
    return render(request,'user/login.html',{})

class LoginView(FormView):
    form_class = LoginForm
    success_url = "posts/"
    template_name = "user/login.html"

    def form_valid(self,form):
        request = self.request
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if request.user.is_authenticated:
                return redirect('posts')

        if user:
            login(request,user)
            return redirect('posts')
        else:
            messages.error(self.request,"Invalid Credentials")
        return super(LoginView,self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'user/register.html' 
    success_url = '/'
