from mercedes.serializers import DynamicFieldsModelSerializer

from core.models import Model

from .brand import BrandSerializer

class ModelSerializer(DynamicFieldsModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Model
        fields = '__all__'
