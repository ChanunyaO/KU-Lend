from ku_lend.models import *
from django.core.mail import send_mail

from mysite.settings import EMAIL_HOST_USER


def send_confirm(borrower, item, email):
    """Send reminder before the return date."""
    send_mail('Confirm',
                f"""Dear {borrower},
                    Congratulations you are successful to borrow {item}.
                    Don't forget to pick up your {item} and
                    please return the {item} within the returning date.
                    However, if you do not turn in within the return date, the item will calculate the fee automatically.
                Respectfully Yours,
                Ku Lend admin""",
                EMAIL_HOST_USER,
                [email]
                )

    return email