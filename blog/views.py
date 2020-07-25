from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-date')[:5]
    # this is order by date and i want to show latest 5 blogs only in one page

    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # basically this will give me the object with provided model class and the pk primary key
    return render(request, 'blog/detail.html', {'blog': blog})
