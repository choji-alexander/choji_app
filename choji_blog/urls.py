from django.urls import path
from .views import (ArticleViews, ArticleDetailViews, ArticleCreateViews, ArticleUpdateViews, ArticleDeleteViews)


urlpatterns = [
    path('', ArticleViews.as_view(), name='article-view'),
    path('<int:pk>/', ArticleDetailViews.as_view(), name='article-detail'),
    path('create/', ArticleCreateViews.as_view(), name='article-create'),
    path('<int:pk>/update/', ArticleUpdateViews.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteViews.as_view(), name='article-delete'),

]
