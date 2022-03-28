from django.forms import ModelForm, ModelChoiceField
from .models import Complaints
import Authentication.models as auth_model


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
        self.fields['against'] = ModelChoiceField(queryset=auth_model.NonReviewer.objects.all().exclude(user=user))
        self.fields['reviewer'] = ModelChoiceField(queryset=auth_model.Reviewer.objects.all().exclude(user=user))

