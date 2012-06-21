from django.contrib import admin

from customers.models import Company, Person


class PersonAdmin(admin.ModelAdmin):
  list_display = ['id','first_name','last_name','company']
  list_filter = ['company']
  list_editable = ['first_name','last_name','company']
  search_fields = ['first_name','last_name','company__name']

class CompanyAdmin(admin.ModelAdmin):
  list_display = ['name', 'website', 'app_id']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
