from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import History, Item


def index(request):
    """Query Data from model"""
    all_item = Item.objects.all()
    latest_item_list = Item.objects.order_by('-item_name')[:5]
    context = {'latest_item_list': latest_item_list}
    return render(request, 'ku_lend/index.html', {'items':all_item})

def borrow_form(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'ku_lend/borrow_form.html', {'item': item})

def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)

def confirm(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return HttpResponse(f"You has borrow {item.item_name}. Please, go to {item.pickup_place}.")