from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicHabitListAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("", HabitListAPIView.as_view(), name="habits-list"),
    path("public/", PublicHabitListAPIView.as_view(), name="habit-public"),
    path("view/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-view"),
    path("edit/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-edit"),
    path("delete/<int:pk>", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
