from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from api.users.models import Publication, Follow, SocialUser
from api.users.serializers import PublicationSerializer, FollowSerializer, SocialUserSerializer


class UserViewSet(mixins.RetrieveModelMixin,   # Los viewset son endpoints que heredan cosas de Django
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()                # pregunta a la base de datos
    serializer_class = UserSerializer            # Serializador
    # Permisos (se fija si es un usuario autenticado o es un usuario de solo lectura).
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


""" class PublicationReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Publication.objects.all()       
    serializer_class = PublicationSerializer
    permission_classes = (IsUserOrReadOnly,) """


class PublicationViewSet(viewsets.ModelViewSet):
    """
    Lograr cualquier acción con una publicacion si sos el usuario dueño
    """
    queryset = Publication.objects.select_related(
        'user',
    )
    serializer_class = PublicationSerializer
    permission_classes = (IsUserOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    # cuando hacemos .object le avisamos que queremos ver los obj del modelo en la base de datos.
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsUserOrReadOnly,)


class SocialUserViewSet(viewsets.ModelViewSet):
    # cuando hacemos .object le avisamos que queremos ver los obj del modelo en la base de datos.
    queryset = SocialUser.objects.all()
    serializer_class = SocialUserSerializer
    permission_classes = (IsUserOrReadOnly,)
