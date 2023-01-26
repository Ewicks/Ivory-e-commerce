from django.contrib import admin
from .models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email'
    )

    ordering = ('name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
