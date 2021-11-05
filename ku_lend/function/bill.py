from datetime import datetime
from django.utils import timezone
import datetime
from ku_lend.models import *
from django.core.mail import send_mail


def send_bill():
    """Send fine."""
    now = timezone.now()
    if now + datetime.timedelta(days=2) > History.return_date:
        fee = 10 * now + datetime.timedelta(days=2) > History.return_date
        send_mail('Reminder',
                  f'Please return {Item.item_name} on {History.return_date} and please paid {fee} baht for the delay',
                  None,
                  [History.borrower_email]
                  )
