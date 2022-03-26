from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('type', 'name', 'email', 'phone', 'nsu_id', 'nsu_card', 'password1', 'password2')
        labels = {
            'type': 'Sign up as',
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'nsu_id': 'NSU ID',
            'nsu_card': 'NSU Card Image',
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
