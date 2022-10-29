from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from reviewer.models import Review
from reviewer.forms import ReviewForm

from reviewer.models import Product


class FeedCreateView(CreateView):
    template_name = 'review/create_feed.html'
    form_class = ReviewForm
    model = Review
    success_url = '/'

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


class FeedUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/update_review.html'
    success_url = '/'


class FeedDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = '/'
