import requests
from config import settings
from django.core.mail import send_mail


def send_mail_message(user_mail, message):
    """
    Отправляет письма об изменении курса для подписчиков
    """
    send_mail(
        subject='Напоминание',
        message=f'Напоминание:\n{message}.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_mail],
        fail_silently=False,
        )

def send_telegram_message(tg_name, message):
    """
    Отправляет сообщение в Telegram.
    """

    params = {
        'chat_id': tg_name,
        'text': message,
    }
    response = requests.post(
        f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage',
        params=params
    )
    response.raise_for_status()
