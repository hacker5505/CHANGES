from django.shortcuts import render, redirect
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        return render(request, 'pages/home.html', context={'home': True})
        # return redirect('superadmin:dashboard') if request.user.is_superuser else redirect('customers:dashboard')
