from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .scripts import Script

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, BookDetailSerializer
# Create your views here.

list_d = []

def index(request):
    if "title" in request.POST:
        try:
            Book.objects.filter(title=request.POST["title"]).delete()
        except:
            pass

    all_books = Book.objects.order_by('title')
    context = {
        'all_books': all_books
    }
    return render(request, 'BookApp/index.html', context)


def detail(request, id_uuid):

    book = Book.objects.get(id_uuid=id_uuid)
    if book:
        return render(request, 'BookApp/detail.html', {'book': book, 'id_uuid': id_uuid})
    else:
        return HttpResponse("Error")


def search(request):
    if "con" in request.POST:
        con = request.POST["con"]
        url = "https://www.googleapis.com/books/v1/volumes?q=" + con
        list_d = Script().parse_json(url)
    else:
        list_d = Script().list_d
    return render(request, 'BookApp/search.html', {'list_d': list_d})


def add(request, list_index):
    dic = Script.list_d[int(list_index)]
    transfer = Script().transfer_data(dic)
    return render(request, 'BookApp/add.html', {'dic': dic, 'transfer': transfer})


@api_view(['GET', 'POST'])
def books_list(request):

    # queryset = Book.objects.all()
    # serializer_class = BookSerializer
    serializer_context = {
        'request': request,
    }
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, context=serializer_context, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def book_detail(request, pk):
    book = Book.objects.get(id_uuid=pk)
    serializer_detail = BookDetailSerializer(instance=book)
    return Response(serializer_detail.data)
