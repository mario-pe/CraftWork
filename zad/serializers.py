from rest_framework import serializers
from .models import CustomerUrl, CustomerFile


class CustomerUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUrl
        fields = ('url', 'password', 'date', 'counter')


class CustomerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFile
        fields = ('file', 'password', 'date', 'counter')