from datetime import datetime
from django.utils import timezone
import datetime
from ku_lend.models import *
from django.core.mail import send_mail

from mysite.settings import EMAIL_HOST_USER


def send_reminder():
    """Send reminder before the return date."""
    now = timezone.now()
    history_list = History.objects.all()
    for history in history_list:
        if now + datetime.timedelta(days=2) == history.return_date:
            send_mail('Reminder',
                f"""Dear {history.borrower},
                    Please return the item within the returning date. However, if you do not turn in within the return date, the item will calculate the fee automatically.
                Respectfully Yours,
                Ku Lend admin""",
                EMAIL_HOST_USER,
                [history.borrower_email]
                )

    return None


# tested sending mail
def try_send_mail():
    send_mail('Reminder',
                """Dear KU student and staff,
                Please return the item within the returning date. However, if you do not turn in within the return date, the item will calculate the fee automatically.
                Respectfully Yours,
                 Ku Lend admin""",
                EMAIL_HOST_USER,
                ['remegac219@ecofreon.com']
                )
    return None