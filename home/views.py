from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
#def index(request):
  #  return render(request, 'home/index.html')#

class HomeView(ListView):
  model = Post
  template_name = 'home/index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


