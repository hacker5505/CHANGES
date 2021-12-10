from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, update_session_auth_hash
from users.models import UserProfile
from .forms import UserPasswordChangeForm, FullNameChangeForm, AccountDeactivationForm


class EditAccountView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
            'name_form': FullNameChangeForm(instance=user_profile)
        }
        return render(request, 'account_setting/edit_account.html', context=context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            if UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.get(user=request.user)
            else:
                user_profile = None
        form = FullNameChangeForm(request.POST, instance=user_profile)
        context = {
            'user_profile': user_profile,
            'name_form': form,
        }
        if form.is_valid():
            form.save()
            context['message'] = True
        return render(request, 'account_setting/edit_account.html', context=context)


class EditSecurityView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
            'password_form': UserPasswordChangeForm(self.request.user)
        }
        return render(request, 'account_setting/edit_security.html', context=context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            if UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.get(user=request.user)
            else:
                user_profile = None
        form = UserPasswordChangeForm(request.user, request.POST)
        context = {
            'user_profile': user_profile,
            'password_form': form,
        }
        if form.is_valid():
            form.save()
            update_session_auth_hash(self.request, form.user)
            context['message'] = True
        return render(request, 'account_setting/edit_security.html', context=context)


class AccountDeactivationView(View):
    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        form = AccountDeactivationForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
