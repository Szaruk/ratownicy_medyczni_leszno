# Generated by Django 3.2.9 on 2021-11-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratownicy_blog', '0003_auto_20211127_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('robocza', 'Robocza'), ('opublikowane', 'Opublikowane')], default='robocze', max_length=13),
        ),
    ]
