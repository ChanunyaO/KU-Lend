from django.urls import path
from django.urls.conf import path
from . import views


app_name = 'ku_lend'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<int:item_id>/results/', views.results, name='results'),
    path('<int:item_id>/vote/', views.vote, name='vote'),
]