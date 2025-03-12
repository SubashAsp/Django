from django import forms
from .models import User
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label="Enter your name")
    email = forms.EmailField(required=True, label="Enter your Email")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Your message")

User = get_user_model()

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, help_text='')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data