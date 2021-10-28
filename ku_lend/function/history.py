from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import History

@login_required(login_url='/accounts/login/')
def user_history(request):
    """See all user history"""
    user = request.user
    user_email = user.email
    context_user_history = History.objects.filter(borrower_email=user_email)
    return render(request, 'ku_lend/profile.html', {"history": context_user_history})

