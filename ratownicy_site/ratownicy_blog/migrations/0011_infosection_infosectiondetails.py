# Generated by Django 3.2.9 on 2022-02-13 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratownicy_blog', '0010_contact_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InfoSection', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InfoSectionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InfoSectionText', models.CharField(max_length=255)),
                ('InfoSection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratownicy_blog.infosection')),
            ],
        ),
    ]