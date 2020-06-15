from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import CommentForm
from .models import Post


class PostView(View):

    def get(self, request):
        news = Post.objects.all()
        paginator = Paginator(news, 9)
        page = request.GET.get('page')
        try:
            content = paginator.page(page)
        except PageNotAnInteger:
            content = paginator.page(1)
        except EmptyPage:
            content = paginator.page(paginator.num_pages)
        contents = {"posts": content}
        return render(request, 'blog/index.html', contents)


class PostDetail(View):
    def get(self, request, slug):
        news = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm()
        comments = news.comments.all()
        content = {'post': news, 'comments': comments, 'comment_form': comment_form}
        return render(request, 'blog/post_detail.html', content)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        news = get_object_or_404(Post, slug=slug)
        comments = news.comments.all()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = news
            new_comment.author = request.user
            new_comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()
        content = {'post': news, 'comments': comments, 'comment_form': comment_form}
        return render(request, 'blog/post_detail.html', content)
