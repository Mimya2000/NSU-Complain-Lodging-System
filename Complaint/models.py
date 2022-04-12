import uuid
from django.contrib.auth import get_user_model
from django.db import models


class Complaints(models.Model):
    Status = (
        ('Submitted', 'Submitted'),
        ('In progress', 'In progress'),
        ('Reviewed', 'Reviewed'),
        ('Declined', 'Declined'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='creator')
    complaint_text = models.TextField(max_length=5000)
    reviewer = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, related_name='reviewer')
    against = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='against')
    against_2 = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, related_name='against2')
    against_3 = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, related_name='against3')
    proof = models.ImageField(upload_to='complaint_proof/')
    status = models.CharField(max_length=100, choices=Status, default='Declined')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


