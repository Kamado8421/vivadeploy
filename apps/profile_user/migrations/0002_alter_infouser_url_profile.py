# Generated by Django 5.0 on 2024-01-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='url_profile',
            field=models.URLField(blank=True, default='https://us.123rf.com/450wm/tatkrav/tatkrav2202/tatkrav220200064/181936570-icono-de-hombre-ilustración-vectorial-imagen-de-archivo.jpg', null=True),
        ),
    ]
