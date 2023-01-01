from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog


def index(request):
    context_dict = {}
    blogs = Blog.objects.order_by('title')
    context_dict['blogs'] = blogs
    return render(request, 'index.html', context=context_dict)


def add_blog(request):
    if request.method == 'GET':
        blog_title = request.GET.get('blog_title')
        if blog_title:
            Blog.objects.create(title=blog_title, likes=0)
            return JsonResponse({'status': 'created'})
        else:
            return JsonResponse({'status': 'failed'})


def increment_likes(request):
    if request.method == 'GET':
        blog_id = request.GET.get('blog_id')
        if blog_id:
            blog = Blog.objects.get(id=int(blog_id))
            if blog:
                likes = blog.likes + 1
                blog.likes = likes
                blog.save()
        return JsonResponse({'total_likes': likes})


def delete_blog(request):
    if request.method == 'GET':
        blog_id = request.GET.get('blog_id')
        if blog_id:
            blog = Blog.objects.get(id=int(blog_id))
            if blog:
                blog.delete()
                return JsonResponse({'status': "deleted"})
            else:
                return JsonResponse({'status': "error"})
