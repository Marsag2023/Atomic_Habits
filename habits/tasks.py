from celery import shared_task
from datetime import datetime, timedelta
from .models import Habit
from .services import send_telegram_message, send_mail_message


@shared_task
def check_habits_and_send_reminders():
    # Проверка, истек ли срок действия привычки
    habits = Habit.objects.all()
    for habit in habits:
        if habit.frequency != 0 and habit.time.date() == datetime.now().today():
            user_message = f"Я буду {habit.action} в {habit.time} в {habit.place}\n"
            if habit.sing_pleasant:
                user_message += f" Не забудьте про  {habit.reward}"
            send_mail_message(habit.owner.email, user_message)
            if habit.owner.tg_name is not None:
                send_telegram_message(habit.owner.tg_name, user_message)
            habit.time += timedelta(days=1)
            habit.frequency -= 1
            habit.save()
