from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@test.ru", password="12345")
        self.habit = Habit.objects.create(
            owner=self.user,
            place="TestPlace",
            time="2024-07-20T10:00",
            action="TestAction",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-view", args=[self.habit.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habit_create(self):
        url = reverse("habits:habit-create")
        data = {
            "place": "Test1Place",
            "action": "Test1Action",
            "time": "2024-07-20T10:00",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertTrue(Habit.objects.all().exists())

    def test_habit_update(self):
        url = reverse("habits:habit-edit", args=[self.habit.pk])
        data = {"place": "AnotherPlace"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "AnotherPlace")

    def test_habit_destroy(self):
        url = reverse("habits:habit-delete", args=[self.habit.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "place": "TestPlace",
                    "time": "2024-07-20T10:00:00Z",
                    "action": "TestAction",
                    "sing_pleasant": False,
                    "frequency": 1,
                    "reward": None,
                    "completion_time": 120,
                    "sing_publicity": False,
                    "owner": 3,
                    "linked_habit": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_public(self):
        url = reverse("habits:habit-public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
