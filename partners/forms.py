from django import forms
from users.models import UserProfile
from partners.models import Category


class DateInput(forms.DateInput):
    input_type = 'date'


class PartnerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['placeholder'] = 'Enter your Bio'
        self.fields['birth_date'].widget = DateInput()
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control custom-select'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter your Address'
        self.fields['organization'].widget.attrs['class'] = 'form-control'
        self.fields['organization'].widget.attrs['placeholder'] = 'Enter your Organization'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your Phone Number'
        self.fields['language'].widget.attrs['class'] = 'form-control'
        self.fields['id_card_front'].required = True
        self.fields['id_card_back'].required = True
        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.all())
        self.fields['category'].widget.attrs['class'] = 'form-control custom-select'
        self.fields['category'].required = True
        self.fields['category'].empty_label = 'Choose a category, you cannot change it afterwards'
        self.fields['degree'].widget.attrs['placeholder'] = 'Enter degree or certificate name'
        self.fields['degree'].widget.attrs['class'] = 'form-control'
        self.fields['degree'].required = True
        self.fields['degree_image'].required = True

    bio = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4}), required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'birth_date',
                  'gender', 'address', 'organization', 'phone_number',
                  'language', 'id_card_front', 'id_card_back', 'category', 'degree', 'degree_image']


class PartnerDescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter your Description'

    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 8}), required=False)

    class Meta:
        model = UserProfile
        fields = ['description']
