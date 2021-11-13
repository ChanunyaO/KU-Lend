from ku_lend.models import Item, History
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone


class AddItems(TestCase):
    def setUp(self):
        super().setUp()
        self.item = Item.objects.create(
            item_name="Laptop",
            pickup_place="iup",
            owner="faculty of engineering",
            note="-",
            pub_date=timezone.now() - timedelta(days=1),
            amount_items=20,
            rate_fee=10,
            max_item_each_user=1,
            max_day_each_user=7
        )
        self.item.save()

    def check_item_added(self):
        """test amount of item that added."""
        self.assertEqual(Item.object.count(), 1)

    def check_item_added(self):
        """test laptop already added"""
        self.assertEqual(Item.objects.get(pk=1).item_name, 'Laptop')
        self.assertEqual(Item.objects.get(pk=1).pickup_place, 'iup')
        self.assertEqual(Item.objects.get(pk=1).owner, 'faculty of engineering')
        self.assertEqual(Item.objects.get(pk=1).note, '-')
