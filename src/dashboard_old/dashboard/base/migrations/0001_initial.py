# Generated by Django 4.2.15 on 2024-08-28 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('nb_of_victories', models.IntegerField()),
                ('nb_of_defeats', models.IntegerField()),
                ('badge', models.IntegerField()),
                ('ranking_position', models.IntegerField()),
                ('nb_of_games_played', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponentNickname', models.CharField(max_length=200)),
                ('opponentScore', models.IntegerField()),
                ('myScore', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_history', to='base.stats')),
            ],
        ),
    ]
