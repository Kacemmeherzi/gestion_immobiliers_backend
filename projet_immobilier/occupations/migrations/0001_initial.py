# Generated by Django 5.1.2 on 2024-11-17 21:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_annonces', '0003_annonce_is_negotiable_annonce_lease_duration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation_type', models.CharField(max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('annonce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occupations', to='app_annonces.annonce')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_occupations', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_occupations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
