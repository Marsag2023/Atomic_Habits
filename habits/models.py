from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=200, verbose_name="Место", help_text="Укажите место"
    )
    time = models.DateTimeField(
        auto_now=False,
        verbose_name="Время выполнения  привычки",
        help_text="Укажите время",
    )
    action = models.CharField(
        max_length=250, verbose_name="Действие", help_text="Укажите действие"
    )
    linked_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    sing_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    frequency = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Периодичность в днях",
        help_text="Введите периодичность от 1 до 7",
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="Вознаграждение",
        help_text="Введите вознаграждение",
        **NULLABLE,
    )
    completion_time = models.IntegerField(
        verbose_name="Время на выполнение привычки",
        default=120,
        help_text="Укажите время на исполнение рпривычки, не более 120 секунд",
    )
    sing_publicity = models.BooleanField(
        default=False, verbose_name="Привычка опубликована"
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
