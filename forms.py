from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    cellphone = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label='Your message', widget=forms.Textarea(attrs={"rows":5, 'class':'form-control'}), required=True)

