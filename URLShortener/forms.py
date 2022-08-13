from django import forms

from .models import ShortURL

class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        exclude=[""]
        fields="__all__"

class URLShortenForm(forms.Form):
    original_url = forms.CharField(min_length=8, required=True, help_text="Original URL", widget=forms.TextInput(attrs={"placeholder":"Input Your URL"}))
    url_key = forms.CharField(min_length=7, max_length=7, help_text="Customize Your Shortened URL Key", widget=forms.TextInput(attrs={"placeholder":"Shortened URL Key."}))

class URLGenerateForm(forms.Form):
    original_url = forms.CharField(min_length=8, required=True, help_text="Original URL", widget=forms.TextInput(attrs={"placeholder":"Input Your URL"}))
