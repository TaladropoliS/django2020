from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

# /////////LIBROS/////////LIBROS/////////LIBROS/////////LIBROS/////////LIBROS/////////


def book_home(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)


def book_add(request):
    Book.objects.create(title=request.POST['titulo'], desc=request.POST['descripcion'])
    return redirect('/book')


def book_view(request, op):
    b = Book.objects.get(id=op)
    temp = b.authors.all()
    all_author = Author.objects.all()

    context = {
        "books": Book.objects.get(id=op),
        "authors": temp,
        "add_author": all_author
    }
    return render(request, 'book.html', context)


def author_to_book(request, book_op):

    b = Book.objects.get(id=book_op)
    a = Author.objects.get(id=request.POST['author_to_book'])
    b.authors.add(a)

    return redirect(f'/book/{book_op}')


# /////////AUTOR/////////AUTOR/////////AUTOR/////////AUTOR/////////AUTOR/////////AUTOR///////


def author_add(request):
    Author.objects.create(first_name=request.POST['autorname'],
                          last_name=request.POST['apellido'], note=request.POST['author_note'])
    return redirect('/author')


def author_home(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)


def author_view(request, op):
    a = Author.objects.get(id=op)
    temp = a.books.all()
    all_books = Book.objects.all()
    context = {
        "authors": Author.objects.get(id=op),
        "books": temp,
        "add_book": all_books
    }
    return render(request, 'author.html', context)


def book_to_author(request, author_op):
    a = Author.objects.get(id=author_op)
    b = Book.objects.get(id=request.POST['select_book_to_author'])
    a.books.add(b)
    return redirect(f'/author/{author_op}')
