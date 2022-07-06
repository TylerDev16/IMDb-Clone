from rest_framework import serializers
from watchmate_app.models import *


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True) # returns "__str__" rather than ID
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist_detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    # custom field, not inside model or views
    # def get_len_name(self, object):
    #     return len(object.name)
    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different")
    #     else:
    #         return data
    #
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Movie` instance, given the validated data.
#         """
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Movie` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different")
#         else:
#             return data

# field level validation
# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value
