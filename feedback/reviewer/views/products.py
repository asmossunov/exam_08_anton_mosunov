from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from reviewer.models import Product
from reviewer.forms import ProductForm

from reviewer.models import Review


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        reviews = Review.objects.filter(is_deleted=False, product=product)
        print(reviews)
        context['reviews'] = reviews
        return context


class ProductCreateView(SuccessDetailUrlMixin, CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product


class ProductUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'edit_product.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    template_name = 'delete_confirm.html'
    model = Product
    success_url = reverse_lazy('index')


def category_view(request, category):
    products = Product.objects.filter(product_category=category, is_deleted=False, remains__gt=0)\
        .order_by('product_name')
    find_form = SearchForm()
    context = {
        'category': category,
        'choices': CategoryChoices.choices,
        'find_form': find_form,
        'products': products,
    }
    return render(request, 'categories.html', context)


