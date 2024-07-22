from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from habits.models import Habit
from habits.pagination import MyPagination
from habits.serializer import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser,]
    pagination_class = MyPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.filter(owner=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner | IsAdminUser,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdminUser,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | IsAdminUser,)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(sing_publicity=True)
    pagination_class = MyPagination
