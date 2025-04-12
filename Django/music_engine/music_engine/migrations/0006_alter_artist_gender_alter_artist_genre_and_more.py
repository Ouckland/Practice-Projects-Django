# Generated by Django 5.2 on 2025-04-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_engine', '0005_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=models.CharField(choices=[('MALE', 'ML'), ('FEMALE', 'FM')], default='--'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('Rap', 'RP'), ('REGGAE', 'R&B'), ('Hip-Hop', 'HP'), ('SAD', 'SD')], default='--'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('Rap', 'RP'), ('REGGAE', 'R&B'), ('Hip-Hop', 'HP'), ('SAD', 'SD')], default='--', max_length=50),
        ),
    ]
