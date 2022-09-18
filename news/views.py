from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from news.models import Noticias


class List_articles(ListView):
    model = Noticias
    template_name = 'noticias/list_news.html'

class Detail_article(DetailView):
    model = Noticias
    template_name = 'noticias/detail_news.html'

class Create_article(CreateView):
    model = Noticias
    template_name = 'noticias/create_news.html' 
    fields = '__all__'
    success_url = '/noticias/list-news/'

class Delete_article(DeleteView):
    model = Noticias
    template_name = 'noticias/delete_news.html'
    success_url = '/noticias/list-news/'

