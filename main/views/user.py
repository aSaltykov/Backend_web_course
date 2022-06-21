from main.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


def get_user_data(user):
    return {
        'id': user.id,
        'email': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }


class ProfileList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProfileDetails(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if not user:
            raise exceptions.ValidationError({'id': ['No such user']})

        data = get_user_data(user)
        return Response([data])
