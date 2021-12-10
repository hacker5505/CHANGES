from django.urls import path
from account_setting.views import (
    EditAccountView, EditSecurityView
)


urlpatterns = [
    path('edit_account/', EditAccountView.as_view(), name='edit_account'),
    path('edit_security/', EditSecurityView.as_view(), name='edit_security'),
]
