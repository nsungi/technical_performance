
from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(label='Message', widget=forms.Textarea)
