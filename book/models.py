from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator



class Book(models.Model):
    created_by      =   models.ForeignKey(User, on_delete=models.PROTECT)
    book_title      =   models.CharField(max_length=68)
    cover           =   models.ImageField(upload_to="cover/%Y/%m", null=True)
    book_author     =   models.CharField(max_length=40)
    view_count      =   models.PositiveIntegerField(default=0)
    posted_on       =   models.DateTimeField(auto_now_add=True, null=True)
    synopsis = models.TextField()
    slug        =   models.SlugField(max_length=140, blank=True, unique=True, null=True)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk':self.pk})

    @property
    def get_review(self):
        return self.book_review.all()
def slug_generator(sender, instance, *args, **kargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=Book)


class BookReviews(models.Model):
    author      =   models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp   =   models.DateTimeField(auto_now_add=True)
    content     =   models.TextField()
    review        =   models.ForeignKey(
        'Book', related_name="book_review", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}"
    class Meta:
        ordering =('-timestamp', ) 