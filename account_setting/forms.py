from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import fields
from users.models import CustomUser, UserProfile
from django.core.exceptions import ValidationError
from .models import AccountDeactivation


class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control font-weight-bold text-muted'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control font-weight-bold text-muted'
        self.fields['old_password'].widget.attrs['class'] = 'form-control font-weight-bold text-muted'

    class Meta:
        model = CustomUser
        fields = '__all__'


class FullNameChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control font-weight-bold text-muted'
        self.fields['last_name'].widget.attrs['class'] = 'form-control font-weight-bold text-muted'

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name')

    def clean(self):
        cleaned_data = super(FullNameChangeForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name.isalpha() or last_name.isalpha():
            raise ValidationError("Only letters are allowed!")


class AccountDeactivationForm(forms.ModelForm):
    class Meta:
        model = AccountDeactivation
        fields = '__all__'
