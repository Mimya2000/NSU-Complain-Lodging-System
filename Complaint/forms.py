from django.forms import ModelForm, ModelChoiceField
from .models import Complaints
from django.contrib.auth import get_user_model


class CreateComplaintForm(ModelForm):

    class Meta:
        model = Complaints
        fields = ('against', 'complaint_text', 'proof', 'reviewer')
        labels = {
            'against': 'Complaint Against',
            'complaint_text': 'Write your complaint here...',
            'proof': 'Attach proof (image)',
            'reviewer': 'Choose a reviewer',
        }

    def __init__(self, user, *args, **kwargs):
        super(CreateComplaintForm, self).__init__(*args, **kwargs)
        self.fields['against'] = ModelChoiceField(queryset=get_user_model().objects.all().exclude(email=user).exclude(email='projectwork.testemail@gmail.com'))
        self.fields['reviewer'] = ModelChoiceField(queryset=get_user_model().objects.all().exclude(email=user).exclude(type='Student').exclude(type='Staff'))

