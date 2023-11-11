from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewBlog, CommentForm
from .models import Blog, Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'
    ordering = ['-date_created']


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/newblog.html'
    fields = ['title', 'content', 'content_image']

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.save()
        return redirect('blog:bloglist')


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(
            blog=self.get_object()).order_by('-date_created')
        context['comments'] = comments
        print(self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        comment = Comment(blog=self.get_object(
        ), user=self.request.user, comment=request.POST.get('comment'))
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = NewBlog
    template_name = 'blog/newblog.html'




def addblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        content_image = request.POST.get('content_image')

        newblog = Blog(user=request.user, title=title, content=content, content_image=content_image)
        newblog.save()
        return HttpResponse("Blog Added")


