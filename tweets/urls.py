from django.urls import path
from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
    path('', TweetListView.as_view(), name='tweet_list'),
    path('create/', TweetCreateView.as_view(), name='tweet_create'),
    path('delete/<pk>/', TweetDeleteView.as_view(), name='tweet_delete'),
    path('<pk>/', TweetDetailView.as_view(), name='tweet_detail'),
    path('<pk>/update/', TweetUpdateView.as_view(), name='tweet_update'),

]
