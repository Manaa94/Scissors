from logging import PlaceHolder
from xml.dom.minidom import Attr
from django import forms
from .models import Url


class UrlForm(forms.ModelForm):
    original = forms.URLField(widget=forms.TextInput(
        attrs={'Placeholder': 'example.com/abc/def/ghi'}))
    path = forms.CharField(required=False)

    class Meta:
        model = Url
        fields = ('original', 'path')
