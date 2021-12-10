from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PartnerForm, PartnerDescriptionForm
from users.models import UserProfile
from gigs.models import CompleteGig


class PartnerCreateView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'partner_form': PartnerForm(),
            'user_profile': user_profile,
        }
        return render(request, 'partners/become-a-partner.html', context=context)

    def post(self, request, *args, **kwargs):
        if UserProfile.objects.filter(user=request.user).exists():
            partner = UserProfile.objects.get(user=request.user)
            partner_form = PartnerForm(
                request.POST, request.FILES, instance=partner)
        else:
            partner_form = PartnerForm(request.POST, request.FILES)
        context = {
            'partner_form': partner_form,
        }
        if partner_form.is_valid():
            partner_form = partner_form.save(commit=False)
            if not UserProfile.objects.filter(user=request.user).exists():
                partner_form.user = request.user
            partner_form.seller = True
            partner_form.save()
            return redirect('pages:home')
        return render(request, 'partners/become-a-partner.html', context=context)


class PartnerDescriptionView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=self.request.user)
        context = {
            'description_form': PartnerDescriptionForm(instance=user),
            'user_profile': user,
        }
        return render(request, 'users/account.html', context=context)

    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(user=self.request.user)
        description_form = PartnerDescriptionForm(request.POST, instance=user)
        context = {
            'user_profile': user, 'description_form': description_form,
        }
        if description_form.is_valid():
            description_form.save()
            return redirect('users:account')
        return render(request, 'users/account.html', context=context)


class PartnerDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            if UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.get(user=request.user)
            else:
                user_profile = None

        context = {
            'user_profile': user_profile,
        }
        return render(request, 'partners/seller_dashboard.html', context=context)


class GigsDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        active_gigs = CompleteGig.objects.filter(
            user=user_profile, active=True)
        for i in active_gigs:
            print(i)
        draft_gigs = CompleteGig.objects.filter(
            user=user_profile, active=False)
        context = {
            'user_profile': user_profile,
            'active_gigs': active_gigs,
            'draft_gigs': draft_gigs
        }
        return render(request, 'partners/gig.html', context=context)


class EarningsDashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            if UserProfile.objects.filter(user=request.user).exists():
                user_profile = UserProfile.objects.get(user=request.user)
            else:
                user_profile = None

        context = {
            'user_profile': user_profile,
        }
        return render(request, 'partners/earning.html', context=context)
