from rest_framework import serializers, exceptions
from .models import User
from api.users.models import SocialUser, Publication, Follow
from django.contrib.auth.models import AnonymousUser


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
    user = SocialUserSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'user',)

    def create(self, validated_data):
        user = (self.context.get("request", None)).user

        if user and not isinstance(user, AnonymousUser):
            validated_data["user"] = SocialUser.objects.get(user=user)
        else:
            raise exceptions.NotAuthenticated("No es posible crear una publicación como usuario anónimo")

        publication = Publication.objects.create(**validated_data)
        return publication
