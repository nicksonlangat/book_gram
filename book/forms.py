from django import forms
from .models import BookReviews


class BookReview(forms.ModelForm):
    content = forms.CharField(widget=(forms.Textarea(attrs={
        'class':'',
        'rows':'8'
    })))
    class Meta:
        model = BookReviews
        fields = ['content',]