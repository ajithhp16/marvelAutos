from django.contrib import admin
from .models import Users

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "last_name", "users_slug", "dob", "contact_number", "mail_address", "address",)
    
admin.site.register(Users, UserAdmin)