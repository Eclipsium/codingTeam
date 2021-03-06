from django.test import TestCase

from foods.models import Food
from foods.models import FoodCategory


class FoodTestCase(TestCase):
    def setUp(self):
        # Должна быть 1 кола
        FoodCategory.objects.create(name_ru="Напитки")
        # Пустая категория, не дожна отображаться
        FoodCategory.objects.create(name_ru="Салаты")
        # Категория с неопубликованной едой, не должна отображаться
        FoodCategory.objects.create(name_ru="Горячее")

        Food.objects.create(
            category_id=1,
            name_ru="Кола",
            code=100,
            internal_code=100,
            cost=123.50,
            is_publish=True,
        )

        Food.objects.create(
            category_id=1,
            name_ru="Пепси",
            code=100,
            internal_code=200,
            cost=123.50,
            is_publish=False,
        )

        Food.objects.create(
            category_id=3,
            name_ru="Бургер",
            code=100,
            internal_code=300,
            cost=123.50,
            is_publish=False,
        )

        Food.objects.create(
            category_id=3,
            name_ru="Картошка фри",
            code=100,
            internal_code=400,
            cost=123.50,
            is_publish=False,
        )

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_food_category(self):
        response = self.client.get("/api/v1/foods/")
        self.assertEqual(response.status_code, 200)

        # Должна быть всего 1 категория
        self.assertEqual(len(response.data), 1)

        # И одна еда
        self.assertEqual(len(response.data[0]["foods"]), 1)
