from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, response
from django.template import loader

from ku_lend.function.confirm_mail import send_confirm
from .models import History, Item
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ku_lend.function.reminder import send_reminder, try_send_mail
from ku_lend.function.bill import send_bill

from django.contrib.auth import get_user_model


def index(request):
    latest_item_list = Item.objects.order_by('-item_name')[:5]
    context = {'latest_item_list': latest_item_list} #danger

    # try_send_mail() #tested
    send_reminder()
    send_bill()

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
    # if int(request.POST["borrow_amount"]) >= item.max_item_each_user:
    #     context = {"msg":'Not allow to lend.'}
    #     return render(request, 'ku_lend/borrow_form.html', context)
    history.borrow_amount = request.POST["borrow_amount"]
    item.amount_items -= int(history.borrow_amount)
    item.save()

    history.save()
    send_confirm(history.borrower, history.item, history.borrower_email)
    return response.HttpResponseRedirect(reverse('ku_lend:index'))
