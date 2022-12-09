from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, like_blog

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('like/<int:blog_pk>/', like_blog, name='like'),

]
