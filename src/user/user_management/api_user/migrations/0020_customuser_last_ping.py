# Generated by Django 4.2.16 on 2024-10-29 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0019_merge_20241025_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_ping',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]