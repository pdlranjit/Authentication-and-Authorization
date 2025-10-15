from django.contrib import admin
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display=('id','username','location')
    search_fields=('email',)
    list_filter=('phone_no')