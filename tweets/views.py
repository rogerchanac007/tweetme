from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import TweetModelForm


class TweetUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/tweet_update.html'
    success_url = reverse_lazy('tweet_list')

    def form_valid(self, form):
        if self.request.user == form.instance.user:
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweet_list')


class TweetCreateView(LoginRequiredMixin, CreateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/tweet_create.html'
    success_url = reverse_lazy('tweet_list')
    login_url = '/admin/'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class TweetListView(ListView):
    queryset = Tweet.objects.all()


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'tweets/detail_view.html', context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        'objects': queryset
    }
    return render(request, 'tweets/list_view.html', context)
