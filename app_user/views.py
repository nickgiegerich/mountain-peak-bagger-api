from os import stat
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers, status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from app_user.serializers import UserSerializer

# Create your views here.


class UserProfiles(APIView):
    """
        View for registering, updating, or deleting user profiles
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.get_or_create(user=user)
            data['response'] = "successfully registered a new user."
            data['token'] = Token.objects.get(user=user).key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsers(APIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.id for user in User.objects.all()]
        return Response(usernames)


class UserTokens(APIView):
    """
        View for obtaining the user tokens for authentication

        TODO: need post request to accept username/password and pass back auth token
    """

    def post(self, request):
        try:
            data = {}
            username = request.data['username']
            password = request.data['password']

            user = User.objects.get(username=username)

            if str(user.password) == str(password):
                data['token'] = Token.objects.get(user=user)
                return Response(data)
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
