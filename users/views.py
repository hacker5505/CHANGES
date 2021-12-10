from gigs.models import CompleteGig
from django.http import request
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserForm, ProfileImageForm, UserNameForm
from users.models import UserProfile
from partners.forms import PartnerDescriptionForm


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'signup_form': UserForm(),
            'user_name_form': UserNameForm()
        }
        return render(request, 'users/signup.html', context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        user_name_form = UserNameForm(request.POST)
        context = {
            'signup_form': user_form,
            'user_name_form': user_name_form
        }
        if user_form.is_valid() and user_name_form.is_valid():
            user_form.save()
            user = authenticate(
                request, username=request.POST['email'], password=request.POST['password1'])
            login(request, user)
            user_name_form = user_name_form.save(commit=False)
            user_name_form.user = request.user
            user_name_form.save()
            return redirect('pages:home')
        return render(request, 'users/signup.html', context=context)


class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = UserProfile.objects.get(user=self.request.user)
        except:
            user = None
        active_gigs = CompleteGig.objects.filter(user=user)
        context = {
            'user_profile': user, 'image_form': ProfileImageForm,  'description_form': PartnerDescriptionForm(instance=user), 'active_gigs': active_gigs
        }
        return context


class UserFormView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=self.request.user)
        image_form = ProfileImageForm(request.POST, request.FILES)
        context = {
            'profile': user, 'image_form': image_form,
        }
        if image_form.is_valid():
            if 'profile_image' in request.FILES:
                if UserProfile.objects.filter(user=request.user).exists():
                    user = UserProfile.objects.get(user=request.user)
                    image_form = ProfileImageForm(
                        request.POST, request.FILES, instance=user)
                    image_form.save()
                    return redirect('users:account')
                else:
                    image_form = image_form.save(commit=False)
                    image_form.user = request.user
                    image_form.save()
                    return redirect('users:account')
        return render(request, 'users/account.html', context=context)


class AccountSettingView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            if UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.get(user=request.user)
            else:
                user_profile = None

        context = {
            'profile': user_profile,
        }
        return render(request, 'users/account_setting.html', context=context)
