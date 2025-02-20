
# from http.cookiejar import lwp_cookie_str
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import User
from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect

from django.views.generic import TemplateView
from.forms import UserForm
# Create your views here.

class RegisterView(TemplateView):
    template_name = 'register.html'



    def get(self,request,*args,**kwargs):
        form = UserForm()
        context = {

        'form': form
        }
        return render(request, self.template_name, context)



    def post(self,request,*args,**kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('register successful')

        return HttpResponse('register error'+str(form.errors))


class  LoginView(TemplateView):
    template_name = 'login.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse('invalid email or password')

        if user.check_password(password):
            return redirect('http://127.0.0.1:8000/blog/')
        else:
            return HttpResponse('invalid email or password')