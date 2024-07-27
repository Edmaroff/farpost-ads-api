from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView


urlpatterns = [
    path("ads/", AdvertisementListView.as_view(), name="ads_list"),
    path("ads/<int:id>/", AdvertisementDetailView.as_view(), name="ads_detail"),
]
