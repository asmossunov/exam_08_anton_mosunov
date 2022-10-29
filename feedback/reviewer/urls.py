from django.contrib import admin
from django.urls import path
from reviewer.views.base import ProductsIndexView
from reviewer.views.products import category_view, ProductCreateView, ProductView, \
    ProductUpdateView, ProductDeleteView
from reviewer.views.feeds import FeedCreateView, FeedUpdateView, FeedDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductsIndexView.as_view(), name='index'),
    path('products/', ProductsIndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('products/<str:category>', category_view, name='list_by_category'),

    # path('feeds/', FeedsIndexView.as_view(), name='feeds'),
    # path('feeds/<int:pk>', FeedView.as_view(), name='feed_detail'),
    path('feed/<int:pk>/create/', FeedCreateView.as_view(), name='feed_create'),
    path('feeds/<int:pk>/update/', FeedUpdateView.as_view(), name='feed_update'),
    path('feeds/<int:pk>/delete/', FeedDeleteView.as_view(), name='feed_delete'),
    path('feeds/<int:pk>/confirm-delete/', FeedDeleteView.as_view(), name='confirm_delete'),


]
