from django.urls import path
from .views import ListUserPeaks

urlpatterns = [
    path('user/<int:id>/', ListUserPeaks.as_view()),
    path('user/peak/<int:peakId>', ListUserPeaks.as_view())
]
