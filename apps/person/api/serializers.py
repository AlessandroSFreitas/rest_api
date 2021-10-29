from apps.person.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    # family_id = serializers.IntegerField()

    class Meta:
        model = Person

        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'nick_name',
            'mother_name',
            'weight',
            'height',
            'race',
            'another_race',
            'gender',
            'another_gender',
            'blood_type',
            'family_id',
        ]
