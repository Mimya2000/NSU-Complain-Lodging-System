from django.forms import ModelForm, ModelChoiceField
from .models import Complaints
from django.contrib.auth import get_user_model


class CreateComplaintForm(ModelForm):

    class Meta:
        model = Complaints
        fields = ('against', 'against_2', 'against_3', 'complaint_text', 'proof', 'reviewer')
        labels = {
            'complaint_text': 'Write your complaint here...',
            'proof': 'Attach proof (image)',
            'reviewer': 'Choose a reviewer',
        }

    def __init__(self, user, *args, **kwargs):
        super(CreateComplaintForm, self).__init__(*args, **kwargs)
        self.fields['against'] = ModelChoiceField(queryset=get_user_model().objects.all().exclude(email=user).exclude(email='projectwork.testemail@gmail.com'))
        self.fields['against_2'] = ModelChoiceField(required=False, queryset=get_user_model().objects.all().exclude(email=user).exclude(email='projectwork.testemail@gmail.com'))
        self.fields['against_3'] = ModelChoiceField(required=False, queryset=get_user_model().objects.all().exclude(email=user).exclude(email='projectwork.testemail@gmail.com'))
        self.fields['reviewer'] = ModelChoiceField(required=False, queryset=get_user_model().objects.all().exclude(email=user).exclude(type='Student').exclude(type='Staff'))


class EditComplaintReviewerForm(ModelForm):
    class Meta:
        model = Complaints
        fields = ('reviewer', 'status')
        labels = {
            'reviewer': 'Reviewer',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        super(EditComplaintReviewerForm, self).__init__(*args, **kwargs)
        self.fields['reviewer'] = ModelChoiceField(required=False, queryset=get_user_model().objects.all().exclude(type='Student').exclude(type='Staff'))


class EditComplaintNonReviewerForm(ModelForm):
    class Meta:
        model = Complaints
        fields = ('complaint_text', 'proof')
        labels = {
            'complaint_text': 'Text',
            'proof': 'Proof',
        }
