from django.shortcuts import render
from django.views.generic import View
from users.models import UserProfile
from partners.models import Category
from gigs.models import CompleteGig
from django.contrib.postgres.search import SearchVector


class HomeView(View):
    def get(self, request, *args, **kwargs):
        gigs = CompleteGig.objects.all()
        if not request.user.is_authenticated:
            user_profile = None
        else:
            user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
            'categories': ''
        }
        categories = []
        for i in gigs:
            if not i.over_view.sub_category.category.name in categories:
                categories.append(i.over_view.sub_category.category.name)
            up_dict = {'categories': categories}
            context.update(up_dict)
        return render(request, 'pages/home.html', context=context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'pages/about.html', context=context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            user_profile = None
        else:
            user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'user_profile': user_profile,
        }
        return render(request, 'pages/contact.html', context=context)
