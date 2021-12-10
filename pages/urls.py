from django.urls import path
from pages.views import HomeView, AboutView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact_us/', ContactView.as_view(), name='contact'),
]
