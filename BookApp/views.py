from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .scripts import Script

# Create your views here.

list_d = []


def index(request):
    all_books = Book.objects.order_by('title')
    context = {
        'all_books': all_books
    }
    return render(request, 'BookApp/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(pk = book_id)
    return render(request, 'BookApp/detail.html', {'book': book})


def results(request, book_id):
    return HttpResponse("Results %s" % book_id)


def search(request):
    con = request.POST["con"]
    url = "https://www.googleapis.com/books/v1/volumes?q=" + con
    list_d = Script().parse_json(url)
    return render(request, 'BookApp/search.html', {'list_d': list_d})


def add(request, list_index):
    dic = Script.list_d[int(list_index)]
    transfer = Script().transfer_data(dic)
    return render(request, 'BookApp/add.html', {'dic': dic, 'transfer': transfer})
