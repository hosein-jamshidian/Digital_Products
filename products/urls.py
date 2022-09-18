from django.contrib import admin
from django.urls import path
from .views import ProductListView,ProductDetailView,CategoryListView,CategoryDetailView,FileListView,FileDetailView



urlpatterns = [
    path("products/",ProductListView.as_view(), name="products-list"),
    path("products/<int:pk>/",ProductDetailView.as_view(), name="product-detail"),

    path("products/<int:product_id>/categories/",CategoryListView.as_view(), name="categories-list"),
    path("products/<int:product_id>/categories/<int:pk>/",CategoryDetailView.as_view(), name="categories-detail"),

    path("products/<int:product_id>/files/",FileListView.as_view(), name="files-list"),
    path("products/<int:product_id>/files/<int:pk>",FileDetailView.as_view(), name="files-detail"),
]