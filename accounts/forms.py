from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
        }) 
    )
    last_name = forms.CharField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
        }) 
    )
    username = forms.CharField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
        }) 
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            "class":"form-control",
        }) )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
        })
        )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
        })
        )