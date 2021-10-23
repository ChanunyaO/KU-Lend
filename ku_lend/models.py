import datetime

from django.db import models
from django.utils import timezone


# class Fee(models.Model):
#     """fee"""
#     start_date = models.DateTimeField()
#     last_date = models.DateTimeField()
#     fee = 100
#
#     def count_fee(self):
#         if self.last_date > self.start_date:
#             return (self.last_date - self.start_date) * self.fee
