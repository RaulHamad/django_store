from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput())
    password = forms.CharField(max_length=32,widget=forms.PasswordInput(),required=True)
