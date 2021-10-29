from apps.family.models import Family
from rest_framework import serializers


class FamilySerializer(serializers.HyperlinkedModelSerializer):
    people = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Family
        fields = ['id', 'family_name', 'people']
