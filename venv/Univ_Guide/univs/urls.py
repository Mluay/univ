from django.urls import path
from .views import index, all_univs, h_basied, filter_univ, news_posts, news_post, advices

urlpatterns = [
    path('', index, name='index'),
    path('univs', all_univs, name='univs'),
    path('h_basied', h_basied, name='h_basied'),
    path('filter_univ', filter_univ, name='filter_univ'),
    path('news_posts', news_posts, name='news_posts'),
    path('news_post/<int:post_id>/', news_post, name='news_post'),
    path('advices', advices, name='advices'),
]