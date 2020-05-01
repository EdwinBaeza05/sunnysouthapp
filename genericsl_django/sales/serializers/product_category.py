""" Serializers Product Category."""

#django
from rest_framework import serializers

#models
from genericsl_django.sales.models import ProductCategory


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        fields = '__all__'

