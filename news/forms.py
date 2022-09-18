from django.views.generic import ListView, DetailView, CreateView, DeleteView
from news.models import Noticias

class List_articles(ListView):
    model = Noticias
    template_name = 'list_news.html'

class Detail_article(DetailView):
    model = Noticias
    template_name = 'detail_news.html'

class Create_article(CreateView):
    model = Noticias
    template_name = 'create_news.html'
    fields = '__all__'
    success_url = '/noticias/list_news/'

class Delete_article(DeleteView):
    model = Noticias
    template_name = 'delete_news.html'
    success_url = '/noticias/list_news/'
