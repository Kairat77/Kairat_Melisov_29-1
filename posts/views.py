from rest_framework import viewsets
from .models import Hashtag, Post
from .serializers import HashtagSerializer, PostSerializer

from django.shortcuts import render, redirect
from posts.models import Post, Hashtag
from posts.forms import PostCreateForm
from rest_framework.schemas import get_schema_view



def main_page_view(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context_data = {"posts": posts}
        return render(request, "posts/posts.html", context=context_data)


def hashtags_view(request):
    if request.method == "GET":
        hashtags = Hashtag.objects.all()
        context_data = {"hashtags": hashtags}
        return render(request, "posts/hashtags.html", context=context_data)


def post_detail_view(request, pk):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return render(request, "posts/detail.html")
    context_data = {"post": post}
    return render(request, "posts/detail.html", context=context_data)


def post_create_view(request):
    if request.method == "GET":
        context_data = {"form": PostCreateForm}
        return render(request, "posts/create.html", context=context_data)
    if request.method == "POST":
        data, file = request.POST, request.FILES
        form = PostCreateForm(data, file)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                rate=form.cleaned_data.get("rate"),
            )
            return redirect("/posts/")
        return render(request, "posts/create.html", context={"form": form})
    


class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    serializer_class = Hashtag

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

