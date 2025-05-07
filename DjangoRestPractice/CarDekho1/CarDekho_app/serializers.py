from rest_framework import serializers
from CarDekho_app.models import CarList


def alphanumaric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError('Only alphanumaric Character are allowed')

# serializers convert complex data into python dict 
class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(read_only=True)
    chachisnumber = serializers.CharField(validators=[alphanumaric])
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    # To create data 
    """
        Create and return a new `CarList` instance, given the validated data.
    """
    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
    
    # """
    #     Update and return an existing `CarList` instance, given the validated data.
    #     """
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.chachisnumber = validated_data.get('chachisnumber',instance.chachisnumber)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
