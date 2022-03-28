import uuid
from django.contrib.auth import get_user_model
from django.db import models


class createComplaint(models.Model):
    Status = (
        ('Submitted', 'Submitted'),
        ('In progress', 'In progress'),
        ('Reviewed', 'Reviewed'),
        ('Declined', 'Declined'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    complaint_text = models.TextField(max_length=5000)
    reviewer = models.CharField(max_length=300, null=True, blank=True)
    against = models.CharField(max_length=300, null=True, blank=True)
    proof = models.ImageField(upload_to='complaint_proof/')
    status = models.CharField(max_length=100, choices=Status, default='Declined')
