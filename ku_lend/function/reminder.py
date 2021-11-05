from datetime import datetime
from django.utils import timezone
import datetime
from ku_lend.models import *
from django.core.mail import send_mail

from mysite.settings import EMAIL_HOST_USER


def send_reminder():
    """Send reminder before the return date."""
    now = timezone.now()
    if now + datetime.timedelta(days=2) == History.return_date:
        send_mail('Reminder',
                  f'Please return the item within the returning date',
                  EMAIL_HOST_USER,
                  [borrower]
                  )
    return None


# tested sending mail
def try_send_mail():
    send_mail('Reminder',
    f'Please return the item within the returning date',
    EMAIL_HOST_USER,
    ['remegac219@ecofreon.com']
    )
    return None