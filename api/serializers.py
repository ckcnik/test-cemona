from cemona.models import Modem
from rest_framework import serializers


# class PopulationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Population
#         fields = ('id', 'country', 'city', 'population')
#         read_only_fields = ('id', 'country', 'city', 'population', )


class ModemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modem
        fields = '__all__'


# class ItemSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('id', 'name', 'categories', 'value_int', 'value_float')
