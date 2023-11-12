from rest_framework import serializers
from profiles.models import UserProfile
from django_grpc_framework import proto_serializers # importing files needed for gRPC
from profiles import profile_pb2 # importing files needed for gRPC

class UserProfileSerializer(serializers.ModelSerializer):
    """
    user profile seralizers for seralizering and deserializing data of user profiles
    """
    class Meta:
        model = UserProfile
        fields = '__all__'
        #   fields = ['username', 'full_name', 'points', 'bg_image_url',
        #             'profile_image_url', 'is_mentor', 'bio', 'company',
        #             'job_title', 'created_at', 'is_active', 'updated_at']
        


# class CreateProfileRequestSerializer(proto_serializers.ProtoSerializer):
#     class Meta:
#         proto_class = profile_pb2.CreateProfileRequest

#     email = proto_serializers.CharField(field_number=1)
#     password = proto_serializers.CharField(field_number=2)


# class CreateProfileResponseSerializer(proto_serializers.ProtoSerializer):
#     class Meta:
#         proto_class = profile_pb2.CreateProfileResponse

#     status = proto_serializers.IntegerField(field_number=1)
#     msg = proto_serializers.CharField(field_number=2)
#     error = proto_serializers.CharField(field_number=3)
