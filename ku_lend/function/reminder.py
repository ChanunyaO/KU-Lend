from datetime import datetime
from django.utils import timezone
import datetime
from ku_lend.models import *
from django.core.mail import send_mail


def send_reminder():
    """Send reminder before the return date."""
    now = timezone.now()
    if now + datetime.timedelta(days=2) >= History.return_date:
        send_mail('Reminder',
                  f'Please return {Item.item_name} on {History.return_date}',
                  None,
                  [History.borrower_email]
                  )
    return None
