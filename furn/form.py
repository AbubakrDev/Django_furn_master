from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from furn.models import Profile , Contact
from dataclasses import fields
from django import forms

User = get_user_model()

class UptadeUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['first_name', 'email']
        
class UptadeProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number']
        
class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2",]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email' , 'choices' , 'mobile' , 'massage']
