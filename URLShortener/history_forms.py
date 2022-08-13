from django import forms

class URLHistoryForm(forms.Form):
    original_url = forms.CharField()
    short_url = forms.CharField()
    created_at = forms.DateTimeField()