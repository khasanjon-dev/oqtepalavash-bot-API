from django.urls import path

from company.views import RegionListAPIView

urlpatterns = [
    path('region/', RegionListAPIView.as_view(), name='region'),
]
