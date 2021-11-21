from ku_lend.models import *

def check_status(item, borrow_date, return_date):
    """check item is avaliable or not."""
    status_list = []
    item_list = Item.object.filter(item=item)
    for status in item_list:
        if status.borrow_date > return_date or status.return_date < borrow_date:
            status_list.append(True)
        else:
            status_list.append(False)
    return all(status_list)
