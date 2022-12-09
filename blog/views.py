from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse

from blog.models import Blog, Like


class BlogListView(ListView):
    model = Blog
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('q', None):
            query_string = self.request.GET.get('q')
            queryset = queryset.filter(Q(title__icontains=query_string) | Q(body__icontains=query_string))
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['is_liked'] = Like.objects.filter(user=self.request.user, blog=self.object).exists()
        return context_data


def like_blog(request, blog_pk):
    if request.user.is_authenticated:
        if Like.objects.filter(blog_id=blog_pk, user=request.user).exists():
            Like.objects.filter(blog_id=blog_pk, user=request.user).delete()
        else:
            Like.objects.create(blog_id=blog_pk, user=request.user)
    return redirect(reverse('blog:detail', args=[blog_pk]))
