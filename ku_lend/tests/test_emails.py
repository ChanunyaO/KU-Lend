from ku_lend.models import Item, History
from ku_lend.function import reminder, confirm_mail
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class ReminderTests(TestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
                                    item_name = "Ipad",
                                    pickup_place = "Computer Department",
                                    owner = "Aj. Annan",
                                    note = "-",
                                    pub_date = timezone.now() - timedelta(days=10),
                                    amount_items = 10,
                                    rate_fee = 20,
                                    max_item_each_user = 1,
                                    max_day_each_user = 10                          
                                    )
        self.item.save()

        self.borrower1 = History.objects.create(
                                        item = self.item,
                                        borrow_date = timezone.now(),
                                        return_date = timezone.now() + timedelta(days=10),
                                        borrower = "Borrower1",
                                        borrower_email = "borrower1@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )
        self.borrower1.save()

        self.borrower2 = History.objects.create(
                                        item = self.item,
                                        borrow_date = timezone.now(),
                                        return_date = timezone.now() + timedelta(days=2),
                                        borrower = "Borrower2",
                                        borrower_email = "borrower2@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )
        self.borrower2.save()

        self.borrower3 = History.objects.create(
                                        item = self.item,
                                        borrow_date = timezone.now() - timedelta(days=4),
                                        return_date = timezone.now() - timedelta(days=1),
                                        borrower = "Borrower3",
                                        borrower_email = "borrower3@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )
        self.borrower2.save()

    def test_before_reminder(self):
        """The server will not send email before the reminder date."""
        reminder_func = reminder.send_reminder()
        self.assertNotIn(self.borrower1.borrower_email, reminder_func)

    def test_2_days_before(self):
        reminder_func = reminder.send_reminder()
        self.assertIn(self.borrower2.borrower_email, reminder_func)
        
    def test_after(self):
        reminder_func = reminder.send_reminder()
        self.assertNotIn(self.borrower3.borrower_email, reminder_func)