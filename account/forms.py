from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    """
    redefined class
    Father AuthenticationForm
    I change attribute widget
    """

    def __init__(self, *args, **kwargs):
        """
        redefined widget i change attribute widget
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Електрона адреса'
        })
        self.fields['username'].label = ''

        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Пароль'
        })
        self.fields['password'].label = ''


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login'
    }))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'repeat password'
    }))

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "Name"
    }))

    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "Surname"
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
