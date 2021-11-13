from ku_lend.models import Item, History
from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

class TestAddItems(TestCase):
    """Test add item"""
    def create_item(self, item_names, pickup_places, owners, notes, pub_dates,
                    amount_items1, rate_fees, max_item_each_users, max_day_each_users):
        return Item.objects.create(
            item_name= item_names,
            pickup_place=pickup_places,
            owner=owners,
            note=notes,
            pub_date=pub_dates,
            amount_items=amount_items1,
            rate_fee=rate_fees,
            max_item_each_user=max_item_each_users,
            max_day_each_user=max_day_each_users
        )

    def setUp(self):
        super().setUp()
        self.item = self.create_item('Laptop', "iup", 'faculty of engineering', "-",
                                             timezone.now() - timedelta(days=10), 20, 10, 1, 7)

        self.item2 = self.create_item("Tablet", "iup", "Aj jittat", "-",
                                     timezone.now() - timedelta(days=10), 20, 10, 1, 7)

        self.item.save()
        self.item2.save()

    def test_item_amount_added(self):
        """test amount of item that added."""
        self.assertEqual(Item.objects.count(), 2)

    def test_check_item_added(self):
        """test laptop already added"""
        self.assertEqual(Item.objects.get(pk=1).item_name, 'Laptop')
        self.assertEqual(Item.objects.get(pk=1).pickup_place, 'iup')
        self.assertEqual(Item.objects.get(pk=1).owner, 'faculty of engineering')
        self.assertEqual(Item.objects.get(pk=1).note, '-')

    def test_item_name_is_none(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.item_name = None
        self.assertRaises(TypeError, Item.objects.get(pk=2).item_name)

    def test_max_item_each_user_string(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.max_item_each_user = "1"
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).max_item_each_user)

    def test_rate_fee_is_string(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.rate_fee = "20"
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).rate_fee)

    def test_amount_item_is_string(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.amount_items = "23"
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).amount_items)

    def test_pub_date_is_string(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.pub_date = "2021/07/12"

        with self.assertRaisesMessage(
                ValidationError,
                '“2021/07/12” value has an invalid format. It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.'
        ):item.save()


    def test_amount_items_is_string(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.owner = 109900
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).owner)

    def test_owner_is_number(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.pickup_place = 398403849
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).pickup_place)

    def test_item_name_is_number(self):
        """item name should not be number"""
        item = Item.objects.get(pk=2)
        item.item_name = 123
        item.save()
        self.assertRaises(TypeError, Item.objects.get(pk=2).item_name)


