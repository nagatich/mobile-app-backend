from mercedes.serializers import DynamicFieldsModelSerializer

from core.models import Brand

class BrandSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
