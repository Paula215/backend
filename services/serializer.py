from rest_framework import serializers
from .models import Service,Image
class ImageSerializer(serializers.ModelSerializer):
    service_name=serializers.SlugRelatedField,
    source='service',
    slug_field='name',
    read_only=True,

    class Meta:
        model=Image
        fields=('__all__')

class ServiceSerializer(serializers.ModelSerializer):
    categories_name=serializers.SlugRelatedField(
        many=True,
        source='categories',
        slug_field='name',
        read_only=True,
    )
    images=ImageSerializer(many=True,read_only=True)
    class Meta:
        model=Service
        fields=('__all__')
