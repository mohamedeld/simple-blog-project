from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    all_blogs = Blog.objects.all()
    return render(request,'blog_app/all_blogs.html',{
        'all_blogs':all_blogs,
    })

def blog_detail(request,id):
    blog = get_object_or_404(Blog,pk=id)

    return render(request,'blog_app/blog.html',{
        'blog':blog,
    })
