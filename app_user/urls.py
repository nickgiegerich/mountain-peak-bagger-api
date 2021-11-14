from django.urls import path, include
from .views import ListUsers, UserTokens, UserProfiles
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('all/', ListUsers.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
]
