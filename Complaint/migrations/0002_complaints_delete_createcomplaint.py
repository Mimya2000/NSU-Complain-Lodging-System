# Generated by Django 4.0.2 on 2022-03-28 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0010_reviewer_nonreviewer_helpingstaff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Complaint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('complaint_text', models.TextField(max_length=5000)),
                ('proof', models.ImageField(upload_to='complaint_proof/')),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('In progress', 'In progress'), ('Reviewed', 'Reviewed'), ('Declined', 'Declined')], default='Declined', max_length=100)),
                ('against', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.nonreviewer')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.reviewer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='createComplaint',
        ),
    ]
