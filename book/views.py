from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from . models import Book
from . forms import BookReview

# Create your views here.



class BookList(ListView):
    model       =   Book
    paginate_by =   10
    ordering    =   '-posted_on'

class BookDetail(DetailView):
    model       =   Book
    form        =   BookReview()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = BookReview(request.POST)
        obj = self.get_object()
        if form.is_valid():
            form.instance.author  = request.user
            form.instance.review = obj
            form.save()
            return redirect(reverse("book_detail", kwargs={
                'pk': obj.pk
            }))

    def get_object(self):
        obj = super(BookDetail, self).get_object()
        obj.view_count += 1
        obj.save()
        return obj
    
    

class BookCreate(LoginRequiredMixin, CreateView):
    model       =   Book
    fields      =   ['book_title','cover','book_author', 'synopsis'] 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model   =   Book
    fields  =   ['book_title','cover','book_author', 'synopsis']

    def test_func(self):
        obj = self.get_object()
        if obj.created_by == self.request.user or self.request.user.superuser:
            return True


class BookDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model       =   Book
    success_url =   '/'

    def test_func(self):
        obj = self.get_object()
        if obj.created_by == self.request.user or self.request.user.superuser:
            return True