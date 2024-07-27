from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Advertisement
    """

    class Meta:
        model = Advertisement
        fields = ["id", "title", "farpost_id", "author", "views_count", "position"]
