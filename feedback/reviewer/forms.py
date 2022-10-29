from django import forms

from reviewer.models import Product


from reviewer.models import Review
from reviewer.models.reviews import min_value_validator, max_value_validator


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_category', 'description', 'image',)
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-input'}),

            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }


class ReviewForm(forms.ModelForm):
    widgets = {
        'product_name': forms.TextInput(attrs={'class': 'form-input'}),

        'text': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

    }

    class Meta:
        model = Review
        fields = ('text', 'score')
        validators = (min_value_validator, max_value_validator)







