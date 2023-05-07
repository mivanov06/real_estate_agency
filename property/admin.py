from django.contrib import admin

from .models import Flat, Complaint, Owner


class AdminFlat(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ['flats']


admin.site.register(Flat, AdminFlat)
admin.site.register(Complaint, AdminComplaint)
admin.site.register(Owner, AdminOwner)
