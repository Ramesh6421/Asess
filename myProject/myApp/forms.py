from django import forms
from .models import RequesterModel,RiderModel 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RiderForm(forms.ModelForm):
    status = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial = False)
    class Meta:
        model = RiderModel 
        fields = '__all__'


class RequesterForm(forms.ModelForm):
    class Meta:
        model = RequesterModel
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    contact = forms.CharField(max_length = 12)
    class Meta:
        model =User 
        fields = ['username','password1','password2','contact']