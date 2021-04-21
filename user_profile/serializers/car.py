from rest_framework import serializers

from user_profile.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = [
            'id',
            'user'
        ]

    def create(self, validated_data):
        car, created = self.Meta.model.objects.get_or_create(**validated_data)
        if not created:
            car.save()
        return car
