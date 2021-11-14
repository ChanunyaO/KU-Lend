from ku_lend.models import Item, History
from ku_lend.function import bill
from django.test import TestCase
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
            borrow_date=timezone.now() - timedelta(days=1),
            return_date=timezone.now(),
            borrower="Borrower1",
            borrower_email="borrower1@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower1.save()

        self.borrower2 = History.objects.create(
            item=self.item,
            borrow_date=timezone.now() - timedelta(days=4),
            return_date=timezone.now(),
            borrower="Borrower2",
            borrower_email="borrower2@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower2.save()

        self.borrower3 = History.objects.create(
            item=self.item,
            borrow_date=timezone.now() - timedelta(days=4),
            return_date=timezone.now() - timedelta(days=2),
            borrower="Borrower3",
            borrower_email="borrower3@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower3.save()

        self.borrower4 = History.objects.create(
            item=self.item,
            borrow_date=timezone.now() - timedelta(days=4),
            return_date=timezone.now() + timedelta(days=2),
            borrower="Borrower4",
            borrower_email="borrower4@test.com",
            borrower_fee=0,
            borrower_paid_status="Not paid",
            borrow_amount=1
        )
        self.borrower3.save()

    def test_return_on_date_fee(self):
        """return on time"""
        now = timezone.now()
        self.borrower1_fee = bill.test_send_bill(now)
        self.assertEqual(0, self.borrower1.borrower_fee)

    def test_return_late(self):
        """test fee """
        now = timezone.now() + timedelta(days=1)
        self.borrower2_fee = bill.test_send_bill(now)
        now = timezone.now() + timedelta(days=2)
        self.borrower3_fee = bill.test_send_bill(now)
        self.assertEqual(10, self.borrower2_fee)
        self.assertEqual(20, self.borrower3_fee)

    def test_not_yet_time(self):
        """test it's not time yet"""
        now = timezone.now()
        self.borrower4_fee = bill.test_send_bill(now)
        self.assertEqual(0, self.borrower4_fee)
