from django.contrib import admin

from .models import contact

class Contact(admin.ModelAdmin):
	list_display = ["__str__", "full_name", "subject", "message"]
	class Meta:
		model = contact
admin.site.register(contact)

# Register your models here.
