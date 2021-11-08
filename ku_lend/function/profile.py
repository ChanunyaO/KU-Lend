from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import History

@login_required(login_url='/accounts/login/')
def profile(request):
    """Show user and history information"""
    User = get_user_model()
    user = User.objects.all()

    history_user = request.user
    history_user_email = history_user.email
    context_user_history = History.objects.filter(borrower_email = history_user_email)

    return render(request, 'ku_lend/profile.html', {"profile": user, "history": context_user_history})
