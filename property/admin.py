from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat')


class LikeInInLine(admin.TabularInline):
    model = Flat.liked_by.through
    raw_id_fields = ('user',)


@admin.register(Flat)
class AdminFlat(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [
        FlatsInline, LikeInInLine
    ]
    fieldsets = (
        ('Адрес', {
            'fields': ('town', 'town_district', 'address', 'floor')
        }),
        ('Информация о квартире', {
            'fields': ('description', 'rooms_number', 'living_area', 'has_balcony', 'construction_year', 'new_building')
        })
    )


@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    list_display = ['name', 'pure_phone']
    raw_id_fields = ['flats']

