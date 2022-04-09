from rest_framework import viewsets, permissions

from foods.models import FoodCategory, Food
from foods.serializers import FoodListSerializer, FoodSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FoodCategory.objects.exclude(food__is_publish=False)
    serializer_class = FoodListSerializer
    permission_classes = [permissions.AllowAny]


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
