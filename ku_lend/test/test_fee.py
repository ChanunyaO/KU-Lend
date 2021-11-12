from ku_lend.models import Item, History
from ku_lend.function import bill
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class FeeTests(TestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
            item_name="Ipad",
            pickup_place="Computer Department",
            owner="Aj. Annan",
            note="-",
            pub_date=timezone.now() - timedelta(days=10),
            amount_items=10,
            rate_fee=20,
            max_item_each_user=1,
            max_day_each_user=10
        )
        self.item.save()

        self.borrower1 = History.objects.create(
            item=self.item,
            borrow_date=timezone.now(),
            return_date=timezone.now() + timedelta(days=10),
            borrower="Borrower1",
            borrower_email="borrower1@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower1.save()

        self.borrower3 = History.objects.create(
            item=self.item,
            borrow_date=timezone.now() - timedelta(days=4),
            return_date=timezone.now() - timedelta(days=1),
            borrower="Borrower3",
            borrower_email="borrower3@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower2.save()

    def test_return_on_date_fee(self):
        """return on time"""

        self.assertEqual(0, self.borrower1.test_send_bill())

    def test_fee(selfs):
        """test fee """

        self.assertEqual(10, self.borrower1.test_send_bill())
