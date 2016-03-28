from cemona.models import Probe, Modem, NetworkAdapter
from rest_framework import serializers


# class ModemListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
#         # Maps for id->instance and id->data item.
#         book_mapping = {book.id: book for book in instance}
#         data_mapping = {item['id']: item for item in validated_data}
#
#         # Perform creations and updates.
#         ret = []
#         for book_id, data in data_mapping.items():
#             book = book_mapping.get(book_id, None)
#             if book is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(book, data))
#
#         # Perform deletions.
#         for book_id, book in book_mapping.items():
#             if book_id not in data_mapping:
#                 book.delete()
#
#         return ret


class ModemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modem
        # fields = ('manufacturer', 'model', 'imei', 'hw', 'fw', 'imsi')
        # read_only_fields = ('imsi', )
        # exclude = ('imei',)
        # validators = []
        # list_serializer_class = ModemListSerializer
        # extra_kwargs = {
        #     "probe": {
        #         "validators": [],
        #     },
        #     "device_id": {
        #         "validators": [],
        #     },
        # }
    # def __init__(self, *args, **kwargs):
    #
    #     # probe = Probe.objects.get(sn=kwargs['data']['sn'])
    #     # probe = kwargs['data']['sn']
    #     # replacing symbol type values on the valid choices from NetworkAdapter model
    #     # for adapter in kwargs['data']['net_adapters']:
    #     #     adapter.update({'type': NetworkAdapter.get_device_type_by_name(adapter['type'])})
    #
    #     # # replacing symbol type values on the valid choices from NetworkAdapter model
    #     # for modem in kwargs['data']['modems']:
    #     #     modem.update({'probe': probe})
    #
    #     # Instantiate the superclass normally
    #     super(ModemSerializer, self).__init__(*args, **kwargs)

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('csw_version', instance.csw_version)
    #     instance.content = validated_data.get('os_version', instance.os_version)
    #     instance.created = validated_data.get('ram_size', instance.ram_size)
    #     instance.created = validated_data.get('sd_size', instance.sd_size)
    #     instance.save()

    # def validate(self, data):
    #     if data['password'] != data.pop('confirm_password'):
    #         raise serializers.ValidationError("Passwords do not match")
    #     return data

    # @classmethod
    # def many_init(cls, *args, **kwargs):
    #     # Instantiate the child serializer.
    #     kwargs['child'] = cls()
    #     # Instantiate the parent list serializer.
    #     return ModemSerializer(*args, **kwargs)
    # def bind(self, *args, **kwargs):
    #     super(ModemSerializer, self).bind(*args, **kwargs)
    #     # do stuff with self.context.
    #     pass

    # def validate(self, attrs):
    #     pass
    #     #Ensure that a `Pin` with board_name=attrs['board']['name'] and item=attrs['item'] does not already exist.


class NetworkAdapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkAdapter
        # fields = '__all__'


class ProbeSerializer(serializers.ModelSerializer):
    # queryset = Modem.objects.all()
    modems = ModemSerializer(many=True)
    net_adapters = NetworkAdapterSerializer(many=True)

    class Meta:
        model = Probe
        # fields = '__all__'
        # validators = []

    def __init__(self, *args, **kwargs):

        # probe = Probe.objects.get(sn=kwargs['data']['sn'])
        # probe = kwargs['data']['sn']

        # replacing symbol type values on the valid choices from NetworkAdapter model
        for adapter in kwargs['data']['net_adapters']:
            adapter.update({'type': NetworkAdapter.get_device_type_by_name(adapter['type'])})

        # # replacing symbol type values on the valid choices from NetworkAdapter model
        # for modem in kwargs['data']['modems']:
        #     modem.update({'probe': probe})

        # Instantiate the superclass normally
        super(ProbeSerializer, self).__init__(*args, **kwargs)
        # self.fields['modems'].default = 4
    #
    # @classmethod
    # def many_init(cls, *args, **kwargs):
    #     # Instantiate the child serializer.
    #     kwargs['child'] = cls()
    #     # Instantiate the parent list serializer.
    #     return ProbeSerializer(*args, **kwargs)

    def create(self, validated_data):
        """
        Saved Probe and  other devices (ethernet, wifi, modems) to DB
        :param validated_data:
        """
        modems = validated_data.pop('modems')
        net_adapters = validated_data.pop('net_adapters')
        probe = Probe.objects.create(**validated_data)

        # saving modems
        for modem in modems:
            modem.update({'probe': probe})
            # Modem.objects.update_or_create(file=File.objects.get(pk=key), result=result_obj, user=result_obj.user,
            #                                      defaults=modem)
            Modem.objects.create(**modem)

        # saving network adapters
        for adapter in net_adapters:
            adapter.update({'probe': probe})
            NetworkAdapter.objects.create(**adapter)

        return probe

    def update(self, instance, validated_data):
        instance.email = validated_data.get('csw_version', instance.csw_version)
        instance.content = validated_data.get('os_version', instance.os_version)
        instance.created = validated_data.get('ram_size', instance.ram_size)
        instance.created = validated_data.get('sd_size', instance.sd_size)
        instance.save()

        # unlink modems for probe
        modems = validated_data.pop('modems')
        modems_imei = [modem['imei'] for modem in modems] if modems else None
        for inst_modem in instance.modems.all():
            if inst_modem.imei not in modems_imei:
                inst_modem.probe = None
                inst_modem.save()

        # Create or update page instances that are in the request
        for modem in modems:
            modem = Modem(probe=instance, **modem)
            modem.save()

        net_adapters = validated_data.pop('net_adapters')
        for adapter in net_adapters:
            NetworkAdapter.objects.update_or_create(probe=instance, **adapter)
            # exist_modem = Modem.objects.get(device_id=modem['device_id'])
            # ModemSerializer(data=modem, instance=exist_modem)
            # Modem.objects.create(**modem)

        return instance

    # def validate(self, attrs):
    #     pass
    #     #Ensure that a `Pin` with board_name=attrs['board']['name'] and item=attrs['item'] does not already exist.
