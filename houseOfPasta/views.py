from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    querySet = Post.objects.filter(statue=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 3
