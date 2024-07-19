from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitValidator(
                field1="linked_habit",
                field2="completion_time",
                field3="sing_pleasant",
                field4="reward",
                field5="frequency",
            )
        ]

        # def create(self, validated_data):
        #     new_habit = Habit.objects.create(**validated_data)
        #     new_habit.owner = self.context['request'].user
        #     new_habit.save()
        #     return new_habit
