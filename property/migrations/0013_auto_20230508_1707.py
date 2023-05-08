# Generated by Django 2.2.24 on 2023-05-08 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='flats', to='property.Flat', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
