from django.contrib import admin
from .models import Cargo, Service, Member, Feature


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'status', 'last_update')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'status', 'last_update')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo', 'status', 'last_update')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'description', 'icon', 'status', 'last_update')
