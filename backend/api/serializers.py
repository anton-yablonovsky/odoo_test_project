from rest_framework import serializers
from .models import Building, Entrance, Apartment, User


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["id", "address", "number"]


class EntranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrance
        fields = ["id", "building", "number"]


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ["id", "entrance", "number"]


class ManagerSerializer(serializers.ModelSerializer):
    buildings = serializers.PrimaryKeyRelatedField(
        queryset=Building.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ["username", "password", "role", "buildings"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        buildings = validated_data.pop("buildings", [])
        user = User.objects.create_user(**validated_data, role="manager")
        user.buildings.set(buildings)
        return user


class GuardSerializer(serializers.ModelSerializer):
    entrances = serializers.PrimaryKeyRelatedField(
        queryset=Entrance.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ["username", "password", "role", "entrances"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        entrances = validated_data.pop("entrances", [])
        user = User.objects.create_user(**validated_data, role="guard")
        user.entrances.set(entrances)
        return user


class InhabitantSerializer(serializers.ModelSerializer):
    apartments = serializers.PrimaryKeyRelatedField(
        queryset=Apartment.objects.all(), many=True, required=False
    )

    class Meta:
        model = User
        fields = ["username", "password", "role", "apartments"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        apartments = validated_data.pop("apartments", [])
        user = User.objects.create_user(**validated_data, role="inhabitant")
        user.apartments.set(apartments)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "role"]
