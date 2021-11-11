from ku_lend.models import Item, History
from ku_lend.function import reminder, confirm_mail, bill
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
        """The server will send email before the reminder date."""
        reminder_func = reminder.send_reminder()
        self.assertIn(self.borrower2.borrower_email, reminder_func)
        
    def test_after(self):
        """The server will not send email before the reminder date."""
        reminder_func = reminder.send_reminder()
        self.assertNotIn(self.borrower3.borrower_email, reminder_func)


class ConfirmTests(TestCase):
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

    def test_not_confirm(self):
        """The mail will not send if the borrower does not comfirm yet."""
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
        self.assertNotEqual(confirm_mail.send_confirm, self.borrower1.borrower_email)

    def test_confirm(self):
        """The mail will send to borrower email after confirm the form."""
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
        confirm = confirm_mail.send_confirm(self.borrower1.borrower, self.item, self.borrower1.borrower_email)
        self.assertEqual(confirm, self.borrower1.borrower_email)


class BillingTests(TestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
                                    item_name = "Ipad",
                                    pickup_place = "Computer Department",
                                    owner = "Aj. Annan",
                                    note = "-",
                                    pub_date = timezone.now() - timedelta(days=20),
                                    amount_items = 10,
                                    rate_fee = 20,
                                    max_item_each_user = 1,
                                    max_day_each_user = 10                          
                                    )
        self.item.save()

        self.borrower1 = History.objects.create(
                                        item = self.item,
                                        borrow_date = timezone.now(),
                                        return_date = timezone.now() + timedelta(days=1),
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
                                        return_date = timezone.now(),
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
                                        return_date = timezone.now() - timedelta(days=10),
                                        borrower = "Borrower3",
                                        borrower_email = "borrower3@test.com",
                                        borrower_fee = 0,
                                        borrower_paid_status = "Not paid",
                                        borrow_amount = 1
                                        )
        self.borrower2.save()

    def test_before_return_date(self):
        """The server will not send email before the return date."""
        billing_func = bill.send_bill()
        self.assertNotIn(self.borrower1.borrower_email, billing_func)

    def test_now(self):
        """The server will not send email on the return date."""
        billing_func = bill.send_bill()
        self.assertNotIn(self.borrower2.borrower_email, billing_func)
        
    def test_after(self):
        """The server will send email after the return date."""
        billing_func = bill.send_bill()
        self.assertIn(self.borrower3.borrower_email, billing_func)