from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Flight, Tickets, Airports


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'phone_number', 'is_staff')


class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_number', 'airline', 'departure_city', 'arrival_city', 'departure_date', 'departure_time', 'seats_count')
    list_filter = ('departure_city', 'arrival_city', 'departure_date')
    search_fields = ('flight_number', 'departure_city', 'arrival_city')
    ordering = ('departure_date', 'departure_time')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'seat_number')
    list_filter = ('flight',)
    search_fields = ('user__username', 'flight__flight_number')


admin.site.register(User, UserAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Tickets, BookingAdmin)
admin.site.register(Airports)
