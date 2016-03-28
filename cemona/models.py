# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
import django.utils.timezone


class Event(models.Model):
    code = models.CharField(unique=True, max_length=10)  # TODO Для чего код нужен?
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
#
#
# class Journal(models.Model):
#     idrec = models.BigIntegerField(primary_key=True)
#     idmodem = models.IntegerField()
#     registered = models.DateTimeField()
#     numactiongroup = models.IntegerField()
#     idregmeasurment = models.BigIntegerField()
#     inserted = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'journal'
#
#
# class Level(models.Model):
#     id = models.AutoField()
#     idmeasur = models.IntegerField(blank=True, null=True)
#     lltd = models.FloatField(blank=True, null=True)
#     lon = models.FloatField(blank=True, null=True)
#     field1 = models.IntegerField(blank=True, null=True)
#     field2 = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'level'
#
#
# class LinkModemParam(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     idmodem = models.ForeignKey('Modem', models.DO_NOTHING, db_column='idmodem')
#     idparam = models.ForeignKey('ModemParam', models.DO_NOTHING, db_column='idparam')
#     value = models.CharField(max_length=50)
#     activated = models.DateTimeField()
#     beggroup = models.IntegerField()
#     endgroup = models.IntegerField(blank=True, null=True)
#     inserted = models.DateTimeField()
#     closed = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'link_modem_param'
#         unique_together = (('idmodem', 'idparam', 'activated'),)


# class LinkProbeParam(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     idprobe = models.ForeignKey('Probe', models.DO_NOTHING, db_column='idprobe')
#     idparam = models.ForeignKey('ProbeParam', models.DO_NOTHING, db_column='idparam')
#     active = models.NullBooleanField()
#     activated = models.DateTimeField()
#     deactivated = models.DateTimeField(blank=True, null=True)
#     value = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'link_probe_param'
#         unique_together = (('idprobe', 'idparam', 'activated'),)


class Measurement(models.Model):
    """
    Model Measurements
    """
    # idrec = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=50)  # todo: Где будем использовать эти значения?
    name = models.CharField(max_length=250)
    codeid = models.IntegerField(blank=True, null=True)  # todo: Для чего это поле?

    class Meta:
        verbose_name = _('Measurement')
        verbose_name_plural = _('Measurements')


class Probe(models.Model):
    """
    Probe model
    """
    sn = models.CharField(unique=True, max_length=50, verbose_name=_(u'Serial number'))
    ram_size = models.IntegerField(verbose_name=_(u'Memory Size'))
    sd_size = models.IntegerField()
    # baseboard_mac = models.CharField(max_length=20)
    os_version = models.CharField(max_length=100)
    csw_version = models.CharField(max_length=100)
    # communication_device = models.CharField(max_length=20, blank=True, null=True)
    # ip_address = models.GenericIPAddressField(blank=True, null=True)
    # ip_mask = models.GenericIPAddressField(blank=True, null=True)
    # ip_gateway = models.GenericIPAddressField(blank=True, null=True)
    # dns = models.GenericIPAddressField(blank=True, null=True)
    # ftp_address = models.GenericIPAddressField(blank=True, null=True)
    # ftp_login = models.CharField(max_length=20, blank=True, null=True)
    # ftp_password = models.CharField(max_length=20, blank=True, null=True)
    # ftp_port = models.IntegerField(blank=True, null=True)
    # ftp_period = models.IntegerField(blank=True, null=True)
    # http_address = models.GenericIPAddressField(blank=True, null=True)
    # http_port = models.IntegerField(blank=True, null=True)
    # http_period = models.IntegerField(blank=True, null=True)
    # critical_sd_size = models.IntegerField(blank=True, null=True)
    # ssid = models.CharField(max_length=10, blank=True, null=True)
    # wifi_security = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wifi_encription = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wifi_password = models.CharField(max_length=20, blank=True, null=True)
    # wifi_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    # ethernet_test_status = models.CharField(max_length=10, blank=True, null=True)
    # wifi_test_status = models.CharField(max_length=10, blank=True, null=True)
    # gps_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # ethernet_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wifi_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # probe_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # work_mode = models.TextField(blank=True, null=True)  # This field type is a guess.
    # target_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    # position_system = models.TextField(blank=True, null=True)  # This field type is a guess.
    # ftp_mode = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        verbose_name = _('Probe')
        verbose_name_plural = _('Probes')


class Modem(models.Model):
    """
    Modem model
    """
    # device_id = models.CharField(max_length=16, blank=True, null=True, verbose_name=_(u'Modem name'))
    imei = models.BigIntegerField(verbose_name=_(u'Modem IMEI'))
    probe = models.ForeignKey(Probe, blank=True, null=True, related_name='modems', verbose_name=_(u'Probe'))
    manufacturer = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u'Modem manufacturer'))
    model = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u'Modem model'))
    hw = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'HW modem'))
    fw = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'FW modem'))
    imsi = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem IMSI'))
    # time_zone = models.CharField(max_length=20, blank=True, null=True,
    #                              verbose_name=_(u'Time Zone'))  # todo: не знаю для чего
    # apn = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN'))
    # apn_user = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN user'))
    # apn_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN password'))
    # ras = models.IntegerField(blank=True, null=True, verbose_name=_(u'Modem RAS number'))
    # status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # test_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # mode = models.TextField(blank=True, null=True)  # This field type is a guess.
    # ethernet_test_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    # wifi_test_status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        verbose_name = _('Modem')
        verbose_name_plural = _('Modems')
        # unique_together = (('probe', 'device_id'),)


class NetworkAdapter(models.Model):
    """
    Model for all devices
    """
    device_id = models.CharField(max_length=16, blank=True, null=True, verbose_name=_(u'Device identifier'))
    probe = models.ForeignKey(Probe, blank=True, null=True, related_name='net_adapters', verbose_name=_(u'Probe'))
    mac = models.CharField(max_length=20)

    # division on the types of devices (ethernet|wifi)
    # slug needed for linking with JSON message from Probe
    ETHERNET = 1
    WIFI = 2
    LINKS = [{'id': ETHERNET, 'name': 'ethernet'}, {'id': WIFI, 'name': 'wifi'}]
    DEVICE_TYPE_CHOICES = (
        (ETHERNET, _("Ethernet")),
        (WIFI, _("WiFi")),
    )
    type = models.IntegerField(choices=DEVICE_TYPE_CHOICES, default=ETHERNET, verbose_name=_(u'Device type'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_(u'Device name'))

    class Meta:
        verbose_name = _('Network adapter')
        verbose_name_plural = _('Network adapters')

    @staticmethod
    def get_device_type_by_name(name):
        """
        Return id type device by name
        """

        type_id = None
        # try:
        for link in NetworkAdapter.LINKS:
            if link['name'] == name:
                type_id = link['id']
                break
        # except IndexError:
        #     raise Exception('Parent category does not exist')
        if not type_id:
            raise Exception('Wrong type network adapter')

        return type_id

# class Ethernet(models.Model):
#     """
#     Model for Ethernet devices
#     """
#     device_id = models.CharField(max_length=16, blank=True, null=True, verbose_name=_(u'Identifier device'))
#     probe = models.ForeignKey(Probe, blank=True, null=True, verbose_name=_(u'Probe'))
#     mac = models.CharField(max_length=16)
#
#     class Meta:
#         verbose_name = _('Ethernet')
#         verbose_name_plural = _('Ethernet')
#
#
# class Wifi(models.Model):
#     """
#     Model for Wifi devices
#     """
#     device_id = models.CharField(max_length=16, blank=True, null=True, verbose_name=_(u'Identifier device'))
#     probe = models.ForeignKey(Probe, blank=True, null=True, verbose_name=_(u'Probe'))
#     mac = models.CharField(max_length=16)
#
#     class Meta:
#         verbose_name = _('Ethernet')
#         verbose_name_plural = _('Ethernet')


class LoggingModem(models.Model):
    """
    Logging at which time the modem was attached to a particular Probe
    """
    probe = models.ForeignKey(Probe, verbose_name=_(u'Modem APN'))
    modem = models.ForeignKey(Modem, verbose_name=_(u'Modem APN'))
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name=_(u'Date created'))

    class Meta:
        verbose_name = _('Logging Modem')
        verbose_name_plural = _('Logging Modems')
        # unique_together = (('idprobe', 'idmodem', 'link_time'),)

# class ModemParam(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     param = models.CharField(unique=True, max_length=50)
#     type_value = models.TextField()  # This field type is a guess.
#     named = models.CharField(max_length=100)
#     paramid = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'modem_param'


# class ProbeParam(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     param = models.CharField(unique=True, max_length=50)
#     type_value = models.TextField()  # This field type is a guess.
#     named = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'probe_param'
#
#
class RegisterAction(models.Model):
    # idrec = models.BigIntegerField(primary_key=True)
    modem = models.ForeignKey(Modem, verbose_name=_(u'Modem'))
    numstatemodem = models.IntegerField()  # TODO Зачем ?
    action = models.ForeignKey(Event)  # TODO Зачем uniq , unique=True?
    idactionvalue = models.IntegerField()  # TODO Что это?
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name=_(u'Date created'))
    # TODO ЗАЧЕМ?
    beggroup = models.IntegerField()
    curgroup = models.IntegerField(blank=True, null=True)
    endgroup = models.IntegerField(blank=True, null=True)
    closed = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('Event registration')
        verbose_name_plural = _('Events registration')
        unique_together = (('modem', 'numstatemodem', 'action', 'idactionvalue'),)


# TODO Для чего вообще используем эту таблицу? 'Таблица регистрации измерений для формирования журнала измерений';
class RegisterMeasurement(models.Model):
    measurement = models.ForeignKey(Measurement, verbose_name=_(u'Measurement'))  # todo: Зачем тут был unique=True ?
    idcodemeasurment = models.IntegerField()  # TODO Что это за поле?
    created = models.DateTimeField(default=django.utils.timezone.now, verbose_name=_(u'Date created'))

    class Meta:
        verbose_name = _('Modem')
        verbose_name_plural = _('Modems')
