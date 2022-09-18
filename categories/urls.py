from django.urls import path
from categories.views import list_categories, create_category


urlpatterns = [
    path("lista/", list_categories, name="list_categories"),
    path("crear-categoria/", create_category, name="create_category"),
]