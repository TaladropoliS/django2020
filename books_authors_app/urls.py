from . import views
from django.urls import path

urlpatterns = [
    path('', views.book_home),
    path('book', views.book_home),
    path('books', views.book_add),
    path('book/<op>', views.book_view),
    path('author', views.author_home),
    path('authors', views.author_add),
    path('author/<op>', views.author_view),
    path('author/book_to_author/<author_op>', views.book_to_author),
    path('book/author_to_book/<book_op>', views.author_to_book),
]
