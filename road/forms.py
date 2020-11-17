from django import forms
from .models import Review

class ReviewForm(forms.Form):
    reviewedby = forms.EmailField(widget=forms.EmailInput(attrs={'readonly':'readonly','class': 'form-control','required':'required','placeholder':'Enter Email'}))
    roadid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'hidden','required':'required'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Write Description'}))