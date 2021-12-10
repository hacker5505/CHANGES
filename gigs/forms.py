from django import forms
from .models import OverView, Pricing, Description, Media


class OverViewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OverViewForm, self).__init__(*args, **kwargs)
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['sub_category'].empty_label = 'Select a sub category'
        self.fields['title'].widget.attrs['class'] = 'title-text'
        self.fields['title'].widget.attrs['placeholder'] = 'do something I am really good at'
        self.fields['search_tags'].widget.attrs['id'] = 'tags'
        self.fields['search_tags'].min_length = 2

    title = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2}), max_length=82, required=True, min_length=16)

    class Meta:
        model = OverView
        fields = ('title', 'sub_category', 'search_tags')


class PricingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PricingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name your package'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter the details of your offering'
        self.fields['revision'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_time'].widget.attrs['placeholder'] = 'Enter the delivery of your offering'
        self.fields['delivery_time'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter a fair price of your offering'

    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, }), max_length=100, required=True)

    class Meta:
        model = Pricing
        fields = '__all__'


class DescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'cke_wrapper'
        self.fields['description'].widget.attrs['id'] = 'editor1'

    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, }), min_length=130)

    class Meta:
        model = Description
        fields = '__all__'


class MediaForm(forms.ModelForm):

    class Meta:
        model = Media
        fields = '__all__'
