from django.urls import path
from .views import List_articles, Detail_article, Create_article, Delete_article


urlpatterns = [
    path("list-news/", List_articles.as_view() , name="list_news"),
    path("detail-news/<int:pk>/", Detail_article.as_view() , name="detail_news"),
    path("create-news/", Create_article.as_view() , name="create_news"),
    path("delete-news/<int:pk>/", Delete_article.as_view() , name="delete_news"),
]