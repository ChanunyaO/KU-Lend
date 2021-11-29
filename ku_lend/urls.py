from django.urls import path
from django.urls.conf import path
from . import views
from .function import profile



app_name = 'ku_lend'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.borrow_form, name='borrow_form'),
    path('<int:item_id>/results/', views.results, name='results'),
    path('<int:item_id>/confirm/', views.confirm, name='confirm'),
    path('<int:id>/<str:item_name>/<int:amount>/cancel/', views.cancel, name='cancel'),
    path('profile/', profile.profile),

]