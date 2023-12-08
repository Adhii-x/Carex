from django.contrib import admin
from .models import About,Service,Work,Testimonial,Team,Blog,Booking,Contact

# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("about_title",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_name",)
    prepopulated_fields = {'slug': ('service_name',)}

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("testimonial_name", "position")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("member_name",)
    prepopulated_fields = {'slug': ('member_name',)}

@admin.register(Blog)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")