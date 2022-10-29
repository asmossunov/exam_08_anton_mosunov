from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Avg
from reviewer.models import Product
from reviewer.forms import ProductForm

from reviewer.models import Review

from reviewer.views.feeds import GroupPermission


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
        avg_rate = Review.objects.filter(product=product).aggregate(avg=Avg('score'))
        context['reviews'] = reviews
        context['avg_rate'] = avg_rate
        return context


class ProductCreateView(GroupPermission, SuccessDetailUrlMixin, CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    model = Product
    groups = ['moderators']


class ProductUpdateView(GroupPermission, SuccessDetailUrlMixin, UpdateView):
    template_name = 'edit_product.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['moderators']


class ProductDeleteView(GroupPermission, DeleteView):
    template_name = 'delete_confirm.html'
    model = Product
    success_url = reverse_lazy('index')
    groups = ['moderators']
