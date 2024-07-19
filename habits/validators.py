from rest_framework.serializers import ValidationError


class HabitValidator:
    def __init__(self, field1, field2, field3, field4, field5):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.field4 = field4
        self.field5 = field5

    def __call__(self, value):

        linked_habit = dict(value).get(self.field1)
        completion_time = dict(value).get(self.field2)
        sing_pleasant = dict(value).get(self.field3)
        reward = dict(value).get(self.field4)
        frequency = dict(value).get(self.field5)

        if linked_habit and reward:
            raise ValidationError(
                "Исключен одновременный выбор связанной привычки и указания вознаграждения"
            )

        elif completion_time and completion_time > 120:
            raise ValidationError("Время выполнения должно быть не больше 120 секунд")

        elif linked_habit:
            if not sing_pleasant:
                raise ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки"
                )

        elif sing_pleasant:
            if reward or linked_habit:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )
        elif frequency and frequency < 1:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
