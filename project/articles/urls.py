from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleLastView.as_view(), name='article_list')
]