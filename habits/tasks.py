from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit

from .services import send_mail_message, send_telegram_message


@shared_task
def check_habits_and_send_reminders():
    """
    Проверяет, истек ли срок действия привычки и отправляет напоминания в Telegram и на почту.
    """

    habits = Habit.objects.all()
    for habit in habits:
        if habit.frequency >= 1 and habit.time.date() == datetime.now().today().date():
            user_message = (
                f"Я буду сегодня {habit.action} в {habit.time.time()} в {habit.place}\n"
            )
            if habit.reward is not None:
                user_message += f" Не забудьте про  {habit.reward}"
            send_mail_message(habit.owner.email, user_message)
            if habit.owner.tg_name:
                send_telegram_message(habit.owner.tg_name, user_message)
            habit.time += timedelta(days=1)
            habit.frequency -= 1
            habit.save()
