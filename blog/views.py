from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog


class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by("-created")
    template_name = "blog/blog.html"
    paginate_by = 6


class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
                "liked": liked,
            },
        )

    def blog(self, request, slug, *args, **kwargs):

        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "liked": liked
            },
        )


class BlogLike(View):

    def blog(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=slug)
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog/blog_detail', args=[slug]))
