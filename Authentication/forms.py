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
            'nsu_id': 'NSU Id',
            'nsu_card': 'NSU Card Image',
        }

        def __init__(self, user, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(user, *args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
