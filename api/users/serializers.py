from rest_framework import serializers
from .models import User
from api.users.models import SocialUser, Publication, Follow


# este es un serializer de lectura (para responses)
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


# este es un serializer de escritura (para requests)
class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class SocialUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialUser
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
