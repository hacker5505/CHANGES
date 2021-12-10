from django import forms


class HomeSearchForm(forms.Form):
    search = forms.CharField(max_length=99, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control border-0 form-control-lg shadow-sm'}))
