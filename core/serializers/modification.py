from mercedes.serializers import DynamicFieldsModelSerializer

from core.models import Modification

from .generation import GenerationSerializer

class ModificationSerializer(DynamicFieldsModelSerializer):
    generation = GenerationSerializer()

    class Meta:
        model = Modification
        fields = '__all__'
