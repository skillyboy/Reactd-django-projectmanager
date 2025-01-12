# Generated by Django 5.1.2 on 2024-10-14 01:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="priority",
            field=models.CharField(
                choices=[("low", "Low"), ("mid", "Mid"), ("high", "High")],
                default="low",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("in_progress", "In Progress"),
                    ("done", "Done"),
                    ("abandoned", "Abandoned"),
                    ("canceled", "Canceled"),
                ],
                default="in_progress",
                max_length=20,
            ),
        ),
    ]
