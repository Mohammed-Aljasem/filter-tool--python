from django import forms  
from .models import Student 

class StudentsForm(forms.ModelForm):
        firstname  = forms.CharField(required=True,label='First name', max_length=100)
        lastname   = forms.CharField(required=True,label='Last name', max_length=100)
        email      = forms.CharField(required=True,label='email', max_length=100)
        gender     = forms.CharField(required=True,label='gender', max_length=100)
        age        = forms.IntegerField(required=True)
  
        class Meta:  
            model = Student 
            fields = [
            'firstname',
            'lastname',
            'email',
            'gender',
            'age'
            ]