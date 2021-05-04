from django.contrib import admin
from alerts import models


class AlertAdmin(admin.ModelAdmin):

    list_display = ['user', 'currency', 'above_or_below', 'price', 'is_completed']

admin.site.register(models.Alert, AlertAdmin)
