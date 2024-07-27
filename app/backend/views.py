from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.permissions import IsAuthenticated


class AdvertisementListView(generics.ListAPIView):
    """
    Представление для получения списка объявлений
    """

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementDetailView(generics.RetrieveAPIView):
    """
    Представление для получения деталей конкретного объявления по его id
    """

    permission_classes = [IsAuthenticated]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    lookup_field = "id"
