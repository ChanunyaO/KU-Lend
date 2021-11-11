from ku_lend.models import Item, History
from ku_lend.function import reminder, confirm_mail
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class ReminderTests(TestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
                                    item_name = "Ipad",
                                    pickup_place = "Computer Department",
                                    owner = "Aj. Annan",
                                    note = "-",
                                    pub_date = datetime.today() - timedelta(days=10),
                                    amount_items = 10,
                                    rate_fee = 20,
                                    max_item_each_user = 1,
                                    max_day_each_user = 10                          
                                    )
        self.item.save()

        self.borrower1 = History.objects.create(
                                        item = self.item,
                                        borrow_date = datetime.today(),
                                        return_date = datetime.today() + timedelta(days=10),
                                        borrower = "Borrower1",
                                        borrower_email = "borrower1@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )
        self.borrower1.save()

        self.borrower2 = History.objects.create(
                                        item = self.item,
                                        borrow_date = datetime.today(),
                                        return_date = datetime.today() + timedelta(days=2),
                                        borrower = "Borrower2",
                                        borrower_email = "borrower2@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )

    def test_before_reminder(self):
        """The server will not send email before the reminder date."""
        reminder_func = reminder.send_reminder()
        self.assertNotIn(self.borrower1.borrower_email, reminder_func)
        