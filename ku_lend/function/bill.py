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
        if now > history.return_date + timedelta(days=1) and history.return_status == False:
            d0 = now
            d1 = history.return_date
            delta = d0 - d1
            history.borrower_fee = history.item.rate_fee * delta.days
            history.save()
            send_mail('Billing',
                      f"""Dear {history.borrower.title()},
                    Please return {history.item} to {history.item.owner.title()} at {history.item.pickup_place} as soon as possible. And unfortunately, \
{history.item}'s rate fee is {history.item.rate_fee} baht per day, so do not forget to pay {history.borrower_fee} baht when return {history.item}.

Respectfully Yours,
        Ku-Lend Admin""",
                      EMAIL_HOST_USER,
                      [history.borrower_email]
                      )
            borrower_list.append(history.borrower_email)

    return borrower_list
