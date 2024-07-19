# Generated by Django 5.0.7 on 2024-07-12 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('jess', '0002_user_nickname_alter_user_id_alter_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_of_victories', models.IntegerField()),
                ('nb_of_defeats', models.IntegerField()),
                ('badge', models.IntegerField()),
                ('ranking_position', models.IntegerField()),
                ('nb_of_games_played', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='jess.user')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
