from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'authy/login.html'
    fields = '__all__'
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('grub') 
    
class RegisterPage(FormView):
    template_name = 'authy/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('login')
    #     return super(RegisterPage, self).get(*args, **kwargs)
    
        