from rest_framework import serializers


class EmwSerializer(serializers.Serializer):
    time = serializers.IntegerField()
    unit = serializers.IntegerField()
    value = serializers.FloatField()
    dev_id = serializers.CharField(max_length=256)
