from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        url = HyperlinkedIdentityField(view_name='book-detail',
                                       lookup_field='pk')
        model = Book
        #fields = '__all__'
        fields = ('url', 'pk',
                  'title', 'authors', 'publishedDate', 'industryIdentifiers', 'pageCount', 'imageLinks', 'language'
                  )


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
