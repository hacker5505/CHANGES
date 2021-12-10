from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.views import (UserCreateView, UserAccountView,
                         UserFormView
                         )
from users.forms import UserLoginForm


urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html',
                                     authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/account/', UserAccountView.as_view(), name='account'),
    path('form/', UserFormView.as_view(), name='form'),
]
