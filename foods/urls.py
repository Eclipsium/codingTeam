from rest_framework import routers

from foods import views

v1_router = routers.DefaultRouter()
v1_router.register('foods', views.FoodCategoryViewSet)
