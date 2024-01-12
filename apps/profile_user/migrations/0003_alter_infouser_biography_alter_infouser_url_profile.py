# Generated by Django 5.0 on 2024-01-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0002_alter_infouser_url_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='biography',
            field=models.TextField(blank=True, default='<Vazio>', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='infouser',
            name='url_profile',
            field=models.URLField(blank=True, default='https://cdn-icons-png.flaticon.com/512/3106/3106807.png', null=True),
        ),
    ]
