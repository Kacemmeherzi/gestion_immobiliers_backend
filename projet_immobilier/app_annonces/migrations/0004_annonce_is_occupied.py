# Generated by Django 5.1.2 on 2024-11-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_annonces', '0003_annonce_is_negotiable_annonce_lease_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='is_occupied',
            field=models.CharField(default='no', max_length=10),
        ),
    ]