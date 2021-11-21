from ku_lend.models import *
from django.core.mail import send_mail
import datetime
from datetime import datetime
from mysite.settings import EMAIL_HOST_USER


def send_confirm(borrower, item, email, return_date, rate_fee):
    """Send reminder before the return date."""
    borrower = str(borrower)
    return_date = datetime.strptime(return_date, '%Y-%m-%d')
    send_mail('Confirm',
                f"""Dear {borrower.title()},
                    Please return the {item} within {return_date.strftime("%d %B, %Y")}. However, if you return {item} late, we will have to charge you for {rate_fee} baht per day.

Respectfully Yours,
        Ku Lend admin""",
                EMAIL_HOST_USER,
                [email]
                )

    return email