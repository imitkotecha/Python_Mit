from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'

class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'