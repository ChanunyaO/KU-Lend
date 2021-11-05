from django.db import models
from ipfs_storage import InterPlanetaryFileSystemStorage


class Item(models.Model):
    """Item's information for admin to fill in."""
    item_name = models.CharField(max_length=200)
    pickup_place = models.CharField(max_length=300)
    owner = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    note = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount_items = models.PositiveSmallIntegerField(default=1)
    item_image = models.ImageField(storage=InterPlanetaryFileSystemStorage())

    def __str__(self):
        return self.item_name


class History(models.Model):
    """Information about borrowing and returning item from borrower."""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    return_date = models.DateTimeField()
    borrower = models.CharField(max_length=50)
    borrower_email = models.EmailField()
    borrower_fee = models.IntegerField(null=True)
    borrower_paid_status = models.CharField(max_length=50)
    #Add note

    def __str__(self):
        return f'{self.item} is borrowed by {self.borrower} from {self.borrow_date} to {self.return_date}'
