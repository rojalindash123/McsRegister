from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,_user_get_permissions
from django import forms
from .models import MyUserAccount
from django.contrib.auth import get_user_model
# MyUserAccount = get_user_model()
# User = get_user_model()
# class SignUpForm(UserCreationForm):
#     email=forms.EmailField(max_length=60)
#     password=forms.CharField(max_length=20)
#     first_name=forms.CharField(max_length=50)
#     last_name=forms.CharField(max_length=50)
#     mobile=forms.CharField(max_length=12)
#     username=None
#     class Meta:
#
#         model=User
#
#         fields=('email','password','first_name','last_name','mobile')


# class OrderForm(ModelForm):
#     class Meta:
#         model=MyUserAccount
#         fields='__all__'


class CreateUserForm(UserCreationForm):
     # username=forms.CharField(max_length=50)
     email = forms.EmailField(max_length=60)
    # password1=forms.CharField(max_length=20)
    # password2 = forms.CharField(max_length=20)
     first_name=forms.CharField(max_length=50)
     last_name=forms.CharField(max_length=50)
     mobile=forms.CharField(max_length=12)
     class Meta:
        # User = get_user_model()
        model=MyUserAccount
        # model=User
        fields=['username','first_name','last_name','email','mobile','password1','password2']

