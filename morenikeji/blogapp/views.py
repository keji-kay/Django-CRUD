from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostListView (generic.ListView):
    Model = Post

class PostCreateView (generic.CreateView):
    Model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView (generic.DetailView):
    Model = Post

class   PostDeleteView (generic.UpdateView):
    Model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostListView (generic.ListView):
    Model = Post
