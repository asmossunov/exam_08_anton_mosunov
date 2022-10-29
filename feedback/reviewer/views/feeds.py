from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from reviewer.models import Review
from reviewer.forms import ReviewForm

from reviewer.models import Product

class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()

class FeedCreateView(CreateView):
    template_name = 'review/create_feed.html'
    form_class = ReviewForm
    model = Review
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)


class FeedAddView(LoginRequiredMixin, CreateView):
    template_name = 'review/add_review.html'
    form_class = ReviewForm
    model = Review

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super(FeedAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class FeedUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/update_review.html'
    success_url = '/'
    groups = ['moderators']

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class FeedDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = '/'
    groups = ['moderators']


    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user