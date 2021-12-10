from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
)
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, UserProfile


def valid_username(value):
    if not value.isalnum():
        raise ValidationError("Only letters & numbers are allowed!")


class UserNameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['class'] = 'form-control'
        self.fields['user_name'].validators = [valid_username]
        self.fields['user_name'].required = True

    class Meta:
        model = UserProfile
        fields = ('user_name',)


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].validators = [valid_username]
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
    username = forms.EmailField()


class ProfileImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = ''

    class Meta:
        model = UserProfile
        fields = ['profile_image']


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'


class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
