# Generated by Django 2.2.24 on 2023-05-04 12:56

from django.db import migrations


def set_new_building_value(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


def set_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_building_value, set_backward),
    ]
