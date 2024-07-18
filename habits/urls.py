from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicHabitListAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("", HabitListAPIView.as_view(), name="habits_list"),
    path("public/", PublicHabitListAPIView.as_view(), name="habit_public"),
    path("view/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_view"),
    path("edit/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_edit"),
    path("delete/<int:pk>", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
