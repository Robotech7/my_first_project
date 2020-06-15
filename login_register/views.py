from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserProfileForm


class SignUp(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login_register/SignUp.html')

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user)
            content = {'key': 'yes'}
            return JsonResponse(content)
        else:
            content = {'data': form.errors}
            return JsonResponse(content)


class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login_register/login.html')

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user)
            content = {'key': 'yes'}
            return JsonResponse(content)
        else:
            content = {'data': form.errors}
            return JsonResponse(content)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:news')


class ProfileView(LoginRequiredMixin, View):
    login_url = 'login_register:login'

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        content = {'forms': form}
        return render(request, 'login_register/profile.html', content)

    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
            content = {'forms': form}
            return render(request, 'login_register/profile.html', content)
        else:
            form = UserProfileForm(instance=request.user)
            content = {'forms': form}
            return render(request, 'login_register/profile.html', content)
