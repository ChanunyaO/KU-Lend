import datetime
from ku_lend.models import *
FEE = 100

def count_fee(last_date, start_date):
    if last_date > start_date:
        return (last_date - start_date) * FEE

