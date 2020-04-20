from django import template
from django.shortcuts import render
from book.models import Book
from django.contrib.auth.models import User
register=template.Library()
@register.simple_tag
def total_books():
	count = Book.objects.all().count()
	return count

@register.simple_tag
def total_users():
	user = User.objects.all().count()
	return user