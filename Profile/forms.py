import Authentication.models as auth_model
from django.forms import ModelForm


class StudentForm(ModelForm):

    class Meta:
        model = auth_model.Student
        fields = ['department', 'program', 'picture']
        labels = {
            'department': 'Department',
            'program': 'Program',
            'picture': 'Profile Picture',
        }


class FacultyForm(ModelForm):
    class Meta:
        model = auth_model.Faculty
        fields = ['department', 'picture']
        labels = {
            'department': 'Department',
            'picture': 'Profile Picture',
        }


class AdminEmployeeForm(ModelForm):
    class Meta:
        model = auth_model.AdminEmployee
        fields = ['office', 'designation', 'picture']
        labels = {
            'office': 'Office',
            'designation': 'Designation',
            'picture': 'Profile Picture',
        }


class HelpingStaffForm(ModelForm):
    class Meta:
        model = auth_model.HelpingStaff
        fields = ['picture']
        labels = {
            'picture': 'Profile Picture',
        }



