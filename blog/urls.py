from django.urls import path

from .views import PostView, PostDetail

app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='news'),
    path('post/<str:slug>', PostDetail.as_view(), name='news_detail')
]
