from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/(?P<id_uuid>[\w\-]+)/$', views.detail, name="detail"),
    url(r'^search/$', views.search, name="search"),
    url(r'^add/(?P<list_index>[0-9]+)/$', views.add, name="add"),

    url(r'^api/$', views.books_list, name="api"),
    url(r'^api/(?P<pk>[\w\-]+)/$', views.book_detail, name="book-detail"),
]
