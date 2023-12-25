from django.contrib import admin
from login.models import ContactUs
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display=('name','email','comment','created_at')
    search_field=('name')



admin.site.register(ContactUs,ExpenseAdmin)