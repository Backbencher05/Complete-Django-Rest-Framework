from rest_framework import serializers
from ..models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class CarListSerializer(serializers.ModelSerializer):
    Review = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = CarList
        fields = "__all__"


class ShowroomSerializer(serializers.ModelSerializer):
    # this is nested seralizer 
    # we have to setup the relationship
    # https://www.django-rest-framework.org/api-guide/relations/
    
    # Note: # this "showrooms" is "related name" we give with forign key

    showrooms = CarListSerializer(many=True,read_only =True)
    # showrooms = serializers.StringRelatedField(many=True)
    # showrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # showrooms = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail'  # jiski bhi details dekhni hai, 
    #                                         # give the name we given in the URL's i.e in "url.py"
    # )
    class Meta:
        model = ShowroomList
        fields = "__all__"


