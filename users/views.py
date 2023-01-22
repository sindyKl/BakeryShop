from django.shortcuts import render, redirect
from django.views import View
from .forms import (
    UserRegisterForm,
    UserLoginForm,
    UserProfileForm,
    ChangePassswordForm
)

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views


class UserRegistration(View):
    template_name = 'users/register.html'

    def get(self, request):
        context = {'title': 'Register', 'form': UserRegisterForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            return redirect('profile')

        context = {'title': 'Register', 'form': form}
        return render(request, self.template_name, context)


class UserLogin(View):
    template_name = 'users/login.html'

    def get(self, request):
        context = {'title': 'Login', 'form': UserLoginForm()} 
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')

        context = {'title': 'Login', 'form': form}
        return render(request, self.template_name, context)


class Profile(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request):
        initial_data = {
            'username': request.user.username,
            'bio': request.user.bio,
            'instagram': request.user.instagram,
        }
        form = UserProfileForm(initial=initial_data)
        context = {'form': form} 
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

        context = {'form': form}
        return render(request, self.template_name, context)


def signout(request):
    logout(request)
    return redirect('home')


class ChangePassword(auth_views.PasswordChangeView):
    template_name='users/password_change.html'
    form_class = ChangePassswordForm
