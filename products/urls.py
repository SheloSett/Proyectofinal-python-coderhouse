from django.urls import path
from products.views import list_products, create_product, update_product, delete_product, search_product

urlpatterns = [
    path("lista/", list_products, name="list_products"),
    path("crear-producto/", create_product, name="create_product"),
    path("update-product/<int:pk>/", update_product, name="update_product"),
    path("delete-product/<int:pk>/", delete_product, name="delete_product"),
    path("search-products/", search_product, name="search_products"),
]