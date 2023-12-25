from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','bio','avatar','contact','gender','birth_date','created','updated')
    search_field=('user')
admin.site.register(Profile,ProfileAdmin)
# Register your models here.