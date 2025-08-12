from django.contrib import admin

# Register your models here.

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'course', 'email', 'contact', 'created_at')
    search_fields = ('name', 'roll_number', 'email')
