from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        #how to design form appying css in form
        widgets = {'name':forms.TextInput(attrs = {'class':'form-control'}),
                   'email':forms.TextInput(attrs={'class':'form-control'}),
                   'password':forms.PasswordInput(attrs = {'class':'form-control'}),
                   'confirm_password':forms.PasswordInput(attrs = {'class':'form-control'}),
                   'gender':forms.Select(attrs = {'class':'form-control'}),
                   'phone_number':forms.TextInput(attrs = {'class':'form-control'}),
                   }
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=UserProfile.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email Already Exists")
        else:
            return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        qs = UserProfile.objects.filter(phone_number = phone_number)
        if qs.exists():
            raise forms.ValidationError("phone_number Already Exists")
        else:
            return phone_number


    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if (password==confirm_password):
            return data
        else:
            raise forms.ValidationError("password doesn't match")

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class':'form-control','placeholder':'Enter Password'}))

class GuestForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Username'}))