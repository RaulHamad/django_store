from django import forms


class Login (forms.ModelForm):
    
    class Meta:
        model = "Login"
        fields = ("username","password")
