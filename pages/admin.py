from django.contrib import admin
from .models import Registration


# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
     list_display = ('id','team_name', 'team_manager')    
     list_display_links = ('id', 'team_name')

admin.site.register(Registration, RegistrationAdmin)