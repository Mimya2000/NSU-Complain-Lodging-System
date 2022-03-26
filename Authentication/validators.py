from django.core.exceptions import ValidationError


def validate_phone(value):
    if len(str(value)) < 11 or len(str(value)) > 11:
        raise ValidationError('Please enter 11 digits of your Phone Number')
    if not str(value).isnumeric():
        raise ValidationError('Please enter only numeric digits in Phone Number')


def validate_id(value):
    if len(str(value)) < 10 or len(str(value)) > 10:
        raise ValidationError('Please enter 10 digits of your NSU ID')
    if not str(value).isnumeric():
        raise ValidationError('Please enter only numeric digits')


