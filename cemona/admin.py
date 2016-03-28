from django.contrib import admin
from .models import Measurement, Probe, Modem, NetworkAdapter


class MeasurementAdmin(admin.ModelAdmin):
    """
    Model Measurements connect to admin panel
    """
    list_display = ('code', 'name', 'codeid')
admin.site.register(Measurement, MeasurementAdmin)


class ProbeAdmin(admin.ModelAdmin):
    """
    Model Probe connect to admin panel
    """
    list_display = ('sn', 'ram_size', 'sd_size', 'os_version', 'csw_version')
admin.site.register(Probe, ProbeAdmin)


class ModemAdmin(admin.ModelAdmin):
    """
    Model Modem connect to admin panel
    """
    list_display = ('imei', 'get_probe', 'manufacturer', 'model')

    def get_probe(self, obj):
        return obj.probe.sn

admin.site.register(Modem, ModemAdmin)


class NetworkAdapterAdmin(admin.ModelAdmin):
    """
    Model NetworkAdapter connect to admin panel
    """
    list_display = ('name', 'device_id', 'get_probe', 'mac', 'type')

    def get_probe(self, obj):
        return obj.probe.sn
admin.site.register(NetworkAdapter, NetworkAdapterAdmin)
