# Generated by Django 4.0.3 on 2022-04-10 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Complaint', '0003_alter_complaints_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='against',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='against', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
