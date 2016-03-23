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


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class Event(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     code = models.CharField(unique=True, max_length=10)
#     name = models.CharField(max_length=250)
#
#     class Meta:
#         managed = False
#         db_table = 'event'
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
#
#
# class LinkProbeModem(models.Model):
#     idrec = models.AutoField(primary_key=True)
#     idprobe = models.ForeignKey('Probe', models.DO_NOTHING, db_column='idprobe')
#     idmodem = models.ForeignKey('Modem', models.DO_NOTHING, db_column='idmodem')
#     link_time = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'link_probe_modem'
#         unique_together = (('idprobe', 'idmodem', 'link_time'),)
#
#
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


# class Measurement(models.Model):
#     """
#     Model Measurements
#     """
#     # idrec = models.AutoField(primary_key=True)
#     code = models.CharField(unique=True, max_length=50)
#     name = models.CharField(max_length=250)
#     codeid = models.IntegerField(blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'measurement'
#     class Meta:
#         verbose_name = _('Measurement')
#         verbose_name_plural = _('Measurements')


class Probe(models.Model):
    # idrec = models.AutoField(primary_key=True)
    serial_number = models.CharField(unique=True, max_length=50)
    memory_size = models.IntegerField()
    sd_size = models.IntegerField()
    mac_address = models.CharField(max_length=16)
    os_version = models.CharField(max_length=100)
    control_sw_version = models.CharField(max_length=100)
    communication_device = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    ip_mask = models.GenericIPAddressField(blank=True, null=True)
    ip_gateway = models.GenericIPAddressField(blank=True, null=True)
    dns = models.GenericIPAddressField(blank=True, null=True)
    ftp_address = models.GenericIPAddressField(blank=True, null=True)
    ftp_login = models.CharField(max_length=20, blank=True, null=True)
    ftp_password = models.CharField(max_length=20, blank=True, null=True)
    ftp_port = models.IntegerField(blank=True, null=True)
    ftp_period = models.IntegerField(blank=True, null=True)
    http_address = models.GenericIPAddressField(blank=True, null=True)
    http_port = models.IntegerField(blank=True, null=True)
    http_period = models.IntegerField(blank=True, null=True)
    critical_sd_size = models.IntegerField(blank=True, null=True)
    ssid = models.CharField(max_length=10, blank=True, null=True)
    wifi_security = models.TextField(blank=True, null=True)  # This field type is a guess.
    wifi_encription = models.TextField(blank=True, null=True)  # This field type is a guess.
    wifi_password = models.CharField(max_length=20, blank=True, null=True)
    wifi_state = models.TextField(blank=True, null=True)  # This field type is a guess.
    ethernet_test_status = models.CharField(max_length=10, blank=True, null=True)
    wifi_test_status = models.CharField(max_length=10, blank=True, null=True)
    gps_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    ethernet_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    wifi_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    probe_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    work_mode = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    position_system = models.TextField(blank=True, null=True)  # This field type is a guess.
    ftp_mode = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        verbose_name = _('Probe')
        verbose_name_plural = _('Probes')


class Modem(models.Model):
    probe = models.ForeignKey(Probe, verbose_name=_(u'Probe'))
    manufacturer = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u'Modem manufacturer'))
    model = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u'Modem model'))
    imei = models.CharField(max_length=16, blank=True, null=True, verbose_name=_(u'Modem IMEI'))
    hw = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'HW modem'))
    fw = models.CharField(max_length=10, blank=True, null=True, verbose_name=_(u'FW modem'))
    imsi_sim = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem IMSI'))
    time_zone = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Time Zone'))  # todo: не знаю для чего
    apn = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN'))
    apn_user = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN user'))
    apn_password = models.CharField(max_length=20, blank=True, null=True, verbose_name=_(u'Modem APN password'))
    ras = models.IntegerField(blank=True, null=True, verbose_name=_(u'Modem RAS number'))
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    test_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    mode = models.TextField(blank=True, null=True)  # This field type is a guess.
    ethernet_test_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    wifi_test_status = models.TextField(blank=True, null=True)  # This field type is a guess.

    # class Meta:
    #     managed = False
    #     db_table = 'modem'
    class Meta:
        verbose_name = _('Modem')
        verbose_name_plural = _('Modems')


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
#
#
# class NemoAqdl(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     aq_mean_dl = models.FloatField(blank=True, null=True)
#     aq_delay_average = models.FloatField(blank=True, null=True)
#     audio_sample_duration_dl = models.IntegerField(blank=True, null=True)
#     mos_type_dl = models.IntegerField(blank=True, null=True)
#     the_event = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_aqdl'
#
#
# class NemoCaa(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     number_of_calls = models.SmallIntegerField(blank=True, null=True)
#     phone_number = models.CharField(max_length=1024, blank=True, null=True)
#     caller_phone_number = models.CharField(max_length=1024, blank=True, null=True)
#     call_type = models.SmallIntegerField(blank=True, null=True)
#     connection_direction = models.SmallIntegerField(blank=True, null=True)
#     call_timeout = models.IntegerField(blank=True, null=True)
#     the_event = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_caa'
#
#
# class NemoCac(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     call_type = models.IntegerField(blank=True, null=True)
#     call_connection_status = models.IntegerField(blank=True, null=True)
#     the_event = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_cac'
#
#
# class NemoCad(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     call_disconnect_status = models.IntegerField(blank=True, null=True)
#     cs_disc_cause = models.IntegerField(blank=True, null=True)
#     the_event = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_cad'
#
#
# class NemoCaf(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     call_failure_cause = models.IntegerField(blank=True, null=True)
#     call_failure_time = models.SmallIntegerField(blank=True, null=True)
#     call_type = models.IntegerField(blank=True, null=True)
#     call_attempt_failure_status = models.IntegerField(blank=True, null=True)
#     the_event = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_caf'
#
#
# class NemoEvent(models.Model):
#     id = models.BigIntegerField()
#     oid = models.BinaryField()
#     current_cell_identification = models.IntegerField(blank=True, null=True)
#     current_channel_number = models.IntegerField(blank=True, null=True)
#     current_mcc = models.SmallIntegerField(blank=True, null=True)
#     current_mnc = models.SmallIntegerField(blank=True, null=True)
#     current_scrambling_code = models.IntegerField(blank=True, null=True)
#     gps_distance = models.IntegerField(blank=True, null=True)
#     gps_height = models.SmallIntegerField(blank=True, null=True)
#     gps_latitude = models.FloatField(blank=True, null=True)
#     gps_longitude = models.FloatField(blank=True, null=True)
#     gps_number_of_satellites = models.SmallIntegerField(blank=True, null=True)
#     gps_time = models.BinaryField(blank=True, null=True)
#     gps_velocity = models.SmallIntegerField(blank=True, null=True)
#     event_id = models.CharField(max_length=1024)
#     time = models.BinaryField(blank=True, null=True)
#     sql_time = models.BinaryField(blank=True, null=True)
#     the_measurement_title = models.CharField(max_length=1024, blank=True, null=True)
#     the_device_imsi = models.CharField(max_length=1024, blank=True, null=True)
#     the_device_imei = models.CharField(max_length=1024, blank=True, null=True)
#     the_serving_system = models.IntegerField(blank=True, null=True)
#     the_serving_band = models.IntegerField(blank=True, null=True)
#     the_serving_type = models.IntegerField(blank=True, null=True)
#     the_serving_technology = models.IntegerField(blank=True, null=True)
#     inserted = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'nemo_event'

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
# class RegisterAction(models.Model):
#     idrec = models.BigIntegerField(primary_key=True)
#     idmodem = models.ForeignKey(Modem, models.DO_NOTHING, db_column='idmodem')
#     numstatemodem = models.IntegerField()
#     idaction = models.ForeignKey(Event, models.DO_NOTHING, db_column='idaction', unique=True)
#     idactionvalue = models.IntegerField()
#     registered = models.DateTimeField()
#     beggroup = models.IntegerField()
#     curgroup = models.IntegerField(blank=True, null=True)
#     endgroup = models.IntegerField(blank=True, null=True)
#     closed = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'register_action'
#         unique_together = (('idmodem', 'numstatemodem', 'idaction', 'idactionvalue'),)
#
#
# class RegisterMeasurement(models.Model):
#     idrec = models.BigIntegerField(primary_key=True)
#     idmeasurement = models.ForeignKey(Measurement, models.DO_NOTHING, db_column='idmeasurement', unique=True)
#     idcodemeasurment = models.IntegerField()
#     inserted = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'register_measurement'
