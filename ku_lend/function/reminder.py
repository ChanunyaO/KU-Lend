from datetime import datetime
from django.utils import timezone
from ku_lend.models import *
from django.core.mail import send_mail
import datetime
from mysite.settings import EMAIL_HOST_USER


def send_reminder():
    """Send reminder before the return date."""
    now = timezone.now()
    history_list = History.objects.all()
    borrower_list = []
    for history in history_list:
        if now + datetime.timedelta(days=2) >= history.return_date and now <= history.return_date and history.return_status == False:
            send_mail('Reminder',
                f"""Dear {history.borrower.title()},
                    Please return {history.item} within {history.return_date.strftime("%d %B, %Y")}. However, if you return {history.item} late, we will have to charge you for {history.item.rate_fee} baht per day.

Respectfully Yours,
        Ku-Lend Admin""",
                EMAIL_HOST_USER,
                [history.borrower_email]
                )
            borrower_list.append(history.borrower_email)

    return borrower_list
