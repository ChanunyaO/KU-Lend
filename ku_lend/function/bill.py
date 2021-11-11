from datetime import timedelta
from django.utils import timezone

from ku_lend.models import *
from django.core.mail import send_mail

from mysite.settings import EMAIL_HOST_USER


def send_bill():
    """Send bill """
    now = timezone.now()
    history_list = History.objects.all()
    borrower_list = []
    for history in history_list:
        if now > history.return_date + timedelta(days=1):
            d0 = now
            d1 = history.return_date
            delta = d0 - d1
            fee = 10 * delta.days
            history.borrower_fee = fee
            history.save()
            send_mail('Billing',
                      f"""Dear {history.borrower},
                    Please return as soon as possible and you have to paid {fee} baht

Respectfully Yours,
        Ku Lend admin""",
                      EMAIL_HOST_USER,
                      [history.borrower_email]
                      )
            borrower_list.append(history.borrower_email)

    return borrower_list

