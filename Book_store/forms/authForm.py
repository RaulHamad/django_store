from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput())
    password = forms.CharField(max_length=32,widget=forms.PasswordInput(),required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput())
    email = forms.CharField(max_length=40,widget=forms.EmailField(),required=True)
    password = forms.CharField(max_length=32,widget=forms.PasswordInput(),required=True)