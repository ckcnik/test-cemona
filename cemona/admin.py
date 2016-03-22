from django.contrib import admin
from .models import Measurement


class MeasurementAdmin(admin.ModelAdmin):
    """
    Model Measurements connect to admin panel
    """
    list_display = ('idrec', 'code', 'name', 'codeid')
admin.site.register(Measurement, MeasurementAdmin)