# Generated by Django 3.2.9 on 2021-11-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratownicy_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='post',
            name='imagePost',
            field=models.ImageField(blank='True', null=True, upload_to='img/'),
        ),
    ]
