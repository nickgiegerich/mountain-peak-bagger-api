import re
from django.db.models import constraints
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from app_user.models import CustomUser
from rest_framework.authtoken.models import Token
from .models import UserPeak

from app_peaks.serializers import UserPeakSerializer

# Create your views here.


class ListUserPeaks(APIView):
    '''
        View for creating, reading, updating, and deleting peaks associated with a user

        Users must pass a token to access this view
    '''
    permission_classes = [IsAuthenticated]

    def verify_user_token(self, token_passed, user_token):
        """
            HELPER: used to verify the token passed in the header request and verify that with the associated user being passed. 

            * token_passed: the token passed in the header
            * user_token: the token associated with the passed user id
        """
        if str(token_passed) == str(user_token):
            return True
        return False

    def get_user(self, id):
        """
            HELPER: method for retrieving a user

            * id: the id of ther user
        """
        try:
            return CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get_user_peaks(self, id, passed_token):
        """
            HELPER: method for retreiving the peaks associated to a user.

            * id: the id of the user
        """
        try:
            user = CustomUser.objects.get(id=id)  # the user to get peaks for

            # the token of the user with id passed by request
            user_token = Token.objects.get(user=user)

            # verify if the token passed matches the user id token
            if self.verify_user_token(token_passed=passed_token, user_token=user_token):
                return UserPeak.objects.filter(user=user)
            else:
                return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        except UserPeak.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        """
            READ: returns a list of peaks created by the user

            * id: the id of the user
        """

        passed_token = request.headers['Authorization'][6:
                                                        ]  # the token passed in the header trimmed to remove 'Token'
        # find the user with the id and verify tokens
        peaks = self.get_user_peaks(id, passed_token)
        serializer = UserPeakSerializer(peaks, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        """
            CREATE: to create a peak object, associated to a user

            * id: id of the user creating the peak object
        """
        user = self.get_user(id)
        data = request.data
        data['user'] = user.id

        serializer = UserPeakSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        """
           TODO UPDATE: used to edit the peak object passed 

            * id: the id of the peak object
        """
        pass
