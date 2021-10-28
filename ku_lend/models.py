import datetime
from django.db import models
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    pickup_place = models.CharField(max_length=300)
    owner = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    note = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount_items = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.item_name} is {self.status} at {self.pickup_place}.'


class History(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    borrower = models.CharField(max_length=50)
    borrower_email = models.EmailField()
    borrower_fee = models.IntegerField()
    borrower_paid_status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.item} is borrowed by {self.borrower} from {self.borrow_date} to {self.return_date}'
