from django.contrib.auth import get_user_model
from django.shortcuts import render


def profile(request):
    User = get_user_model()
    user = User.objects.all()
    return render(request, 'ku_lend/profile.html', {"profile": user})
