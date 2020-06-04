from rest_framework import serializers
from apps.goods.models import MyLookupValue, MyLookupType


class MyLookupTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLookupType
        fields = "__all__"


class MyLookupValueSerializer(serializers.ModelSerializer):
    lookup_type_id = MyLookupTypeSerializer()

    class Meta:
        model = MyLookupValue
        fields = "__all__"
