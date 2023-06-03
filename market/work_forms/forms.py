from django import forms

from .models import People


class CarForm(forms.Form):
    brand = forms.CharField()
    model = forms.CharField()
    price = forms.DecimalField()
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'год-месяц-день'}))


class Rassa(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'

