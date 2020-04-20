from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name="index"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    path('book/create/', views.BookCreate.as_view(), name="create"),
    path('book/<int:pk>/updade/', views.BookUpdate.as_view(), name="update"),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name="delete"),
]
    