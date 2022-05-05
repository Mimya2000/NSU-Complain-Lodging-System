# Generated by Django 4.0.2 on 2022-04-12 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Complaint', '0004_alter_complaints_against_alter_complaints_reviewer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='against_2',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='against2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaints',
            name='against_3',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='against3', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaints',
            name='created',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaints',
            name='reviewer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]