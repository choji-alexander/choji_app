from django.shortcuts import render, get_object_or_404, reverse
from .models import Article
from .forms import ArticleCreationForm
from django.views import View
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)


class ArticleCreateViews(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleCreationForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleViews(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()


class ArticleDetailViews(DetailView):
    template_name = 'article_detail.html'

    def get_object(self):
        my_id = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=my_id)


class ArticleUpdateViews(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleCreationForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        my_id = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=my_id)


class ArticleDeleteViews(DeleteView):
    template_name = 'article_delete.html'
#    queryset = Article.objects.all()
#    success_url = '/blog/'

    def get_object(self):
        my_id = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=my_id)

    def get_success_url(self):
        return reverse('article-view')

