from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response

from ku_lend.function.confirm_mail import send_confirm
from .models import History, Item
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    try:
        user = request.user
        user_email = user.email
        already_borrow = History.objects.filter(borrower_email=user_email,return_status=False)
        already_borrow_name = []
        if(already_borrow is not None):
            for history_data in already_borrow:
                already_borrow_name.append(history_data.item.item_name)
            latest_item_list = Item.objects.exclude(item_name__in=already_borrow_name)
        else:
            latest_item_list = Item.objects.order_by('-item_name')[:]
        context = {'latest_item_list': latest_item_list}
        return render(request, 'ku_lend/index.html', context)
    except:
        latest_item_list = Item.objects.order_by('-item_name')[:]
        context = {'latest_item_list': latest_item_list}
        return render(request, 'ku_lend/index.html', context)


def borrow_form(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'ku_lend/borrow_form.html', {'item': item})


def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)


@login_required(login_url='/accounts/login/')
def confirm(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    history = History(item=item)
    history.borrower = request.user
    history.borrower_email = request.user.email
    history.borrower_paid_status = "Not Paid"
    history.borrower_fee = 0
    history.borrow_date = request.POST['borrow_date']
    history.return_date = request.POST['return_date']

    history.borrow_amount = request.POST["borrow_amount"]
    item.amount_items -= int(history.borrow_amount)

    item.save()
    history.save()
    send_confirm(history.borrower, history.item, history.borrower_email, history.return_date, item.rate_fee)
    return response.HttpResponseRedirect(reverse('ku_lend:index'))

@login_required(login_url='/accounts/login/')
def cancel(request, id, item_name, amount):
    item = get_object_or_404(Item, item_name=item_name)
    item.amount_items += int(amount)
    item.save()
    History.objects.filter(pk=id).delete()
    return response.HttpResponseRedirect('http://127.0.0.1:8000/profile/')