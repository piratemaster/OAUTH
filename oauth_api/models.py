from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    """
    retrieve:
        Return the given dog.

    list:
        Return a list of all dogs.

    create:
        Create a new dog.

    destroy:
        Delete a dog.

    update:
        Update a dog.

    partial_update:
        Update a dog.
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

