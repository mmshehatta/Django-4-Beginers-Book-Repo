from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

from django.http import JsonResponse


# class HomePageView(ListView):
#     model = Post
#     template_name = 'home.html'


# http:localhost:8000
def posts_list(request):

    posts = Post.objects.all()

    data = {
        "Results":list( posts.values("pk", "text"))
        }

    return JsonResponse(data)
