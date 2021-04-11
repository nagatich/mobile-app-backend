from mercedes.serializers import DynamicFieldsModelSerializer

from core.models import Generation

from .model import ModelSerializer

class GenerationSerializer(DynamicFieldsModelSerializer):
    model = ModelSerializer()

    class Meta:
        model = Generation
        fields = '__all__'
