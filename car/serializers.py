from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[
            MaxValueValidator(1914),
            MinValueValidator(1)
        ]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get(
            "manufacturer",
            instance.manufacturer
        )
        instance.model = validated_data.get(
            "model",
            instance.manufacturer
        )
        instance.horse_powers = validated_data.get(
            "horse_powers",
            instance.manufacturer
        )
        instance.is_broken = validated_data.get(
            "is_broken",
            instance.manufacturer
        )
        instance.problem_description = validated_data.get(
            "problem_description",
            instance.manufacturer
        )
        instance.save()
        return instance
