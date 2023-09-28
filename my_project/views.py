from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Author, Book

import requests, json


menu = ["Авторы", "Книги", "Заголовки"]


def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {'books': books, 'menu':menu, 'title':'Книги'})


def book(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book_list.html', context=context)


def detail(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)


def search(request):
    title = request.GET.get('title')
    books = Book.objects.filter(title=title)
    context = {
        'books': books
    }
    return render(request, 'search.html', context)


def update(request, book_id):
    try:
        title = request.GET.get('title')
    except KeyError:
        book = Book.objects.filter(id=book_id).first()
        book.save()
        context = {
            'book': book
    }
        return render(request, 'book_update.html', context=context)
    return redirect('book/')


def delete(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    book.save()
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)

