from django import forms
from .models import Login , Message


class LoginForm(forms.ModelForm):


    class Meta:
        model = Login
        fields = ['name','email','phone']
        widgets ={
            'name':forms.TextInput(attrs={
                'placeholder':'enter your name'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'enter your email'
            }),
             'phone':forms.TextInput(attrs={
                'placeholder':'enter your phone'
            }),
        }



class MessageForm(forms.ModelForm):


    class Meta:
        model = Message
        fields = ['name', 'last','email', 'message']
        widgets ={
            'name':forms.TextInput(attrs={
                'placeholder':'enter your name'
            }),
             'last':forms.TextInput(attrs={
                'placeholder':'enter your name'
            }),
            'email':forms.EmailInput(attrs={
                'placeholder':'enter your email'
            }),
            'message':forms.TextInput(attrs={
                'placeholder':'enter your message'
            }),
        }