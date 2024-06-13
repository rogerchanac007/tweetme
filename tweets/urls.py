from django.urls import path
from .views import tweet_detail_view, tweet_list_view

urlpatterns = [
    path('', tweet_list_view, name='tweet_list'),
    path('1/', tweet_detail_view, name='tweet_detail')
]
