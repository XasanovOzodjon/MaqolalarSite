from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'subject', )
    search_fields = ('fullname', 'subject', 'address')
    ordering = ('fullname',)
