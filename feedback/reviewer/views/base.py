from django.views.generic import ListView

from reviewer.models import Product


class ProductsIndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
