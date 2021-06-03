from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'email', 'contact_date', 'message')
  list_display_links = ('id', 'first_name')
  search_fields = ('first_name', 'email', 'contact_date')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
