from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<book_id>[0-9]+)/results$', views.results, name="results"),
    #url(r'^search/(?P<con>[\w\-]+)/$', views.search, name="search"),
    url(r'^search/$', views.search, name="search"),
    url(r'^add/(?P<list_index>[0-9]+)/$', views.add, name="add"),
]
