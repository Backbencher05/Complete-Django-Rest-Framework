from rest_framework import serializers
from ..models import CarList


# def alphanumaric(value):
#     if not str(value).isalnum():
#         raise serializers.ValidationError('Only alphanumaric Character are allowed')

# serializers convert complex data into python dict 
# class CarSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only = True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # active = serializers.BooleanField(read_only=True)
    # chachisnumber = serializers.CharField(validators=[alphanumaric])
    # price = serializers.DecimalField(max_digits=9, decimal_places=2)
    
# Note: The create() and update() methods define how fully fledged instances
# are "created or modified" when calling serializer.save()
    # # To create data 
"""
    Create and return a new `CarList` instance, given the validated data.
    
    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
"""

    # To Update Data 
"""
    Update and return an existing `CarList` instance, given the validated data.

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.chachisnumber = validated_data.get('chachisnumber',instance.chachisnumber)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
"""
    # here 
        # instance.name etc. is : old data 
        # validated_data is: new data 

#-> Model serializers
# here create() and update() method implimentation already provided we don't need to write manually 
# we can use here model serializers
# all these things Model Serializer will hide 
# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarList
#         fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['name']

class CarSerializer(serializers.ModelSerializer):
    # custom serializers field 
    # discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = CarList
        fields = "__all__"

        
    
    # def get_discounted_price(self,object):
    #     discountedprice = object.price - 2000
    #     return discountedprice

    # field level validation 
    def validated_price(self,value):
        if value <= 20000.00:
            raise serializers.ValidationError("Price must be Greater than 20000.00")
        return value 
    
    # object level validation 
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description must be Different')
        return data

"""
it's important to remember that "ModelSerializer classes" don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

- An automatically determined set of fields.
- Simple default implementations for the create() and update() methods.

"""
