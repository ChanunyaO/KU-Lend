from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Item


def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:5]
    context = {'latest_item_list': latest_item_list}
    return render(request, 'ku_lend/index.html', context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'ku_lend/detail.html', {'item': item})

def results(request, item_id):
    response = "You're looking at the results of item %s."
    return HttpResponse(response % item_id)

def vote(request, item_id):
    return HttpResponse("You're voting on item %s." % item_id)