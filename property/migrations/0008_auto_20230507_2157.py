# Generated by Django 2.2.24 on 2023-05-07 11:57
import phonenumbers
from django.db import migrations


def set_pure_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(pure_phonenumber):
            flat.owner_pure_phone = pure_phonenumber
        else:
            flat.owner_pure_phone = None
        flat.save()


def set_backward_pure_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(owner_pure_phone=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(set_pure_phonenumber, set_backward_pure_phonenumber),
    ]
