# Generated by Django 3.2.9 on 2022-02-13 21:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratownicy_blog', '0008_remove_statisticsimage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank='True')),
                ('photo', models.FileField(upload_to='person/')),
            ],
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MainText', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='text_post',
            field=ckeditor.fields.RichTextField(blank='True'),
        ),
    ]
