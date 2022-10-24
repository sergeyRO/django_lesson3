from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all(),
        'flag': False
    }
    return render(request, template, context)

def date_books_view(request, pub_date):
    template = 'books/books_list.html'
    book = Book.objects.filter(pub_date=pub_date).first()
    try:
        previous_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first().pub_date
    except AttributeError:
        previous_page = False
    try:
        next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first().pub_date
    except AttributeError:
        next_page = False

    context = {
        'book': book,
        'flag': True,
        'previous_page': previous_page,
        'next_page': next_page
    }
    return render(request, template, context)
