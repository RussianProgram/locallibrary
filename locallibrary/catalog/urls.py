from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
		#path('',views.index,name='index')
		url(r'^$',views.index,name='index'),
		url(r"^books/$",views.BookListView.as_view(), name = 'books'),
		url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name = 'book-detail'),
		url(r'^author/$',views.AuthorListView.as_view(), name = 'authors'),
		url(r'^author/(?P<pk>\d+)$',views.AuthorDetailView.as_view(), name = 'author-detail'),
		url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),
		url(r'^borrowed/$',views.LoanedBooksAllListView.as_view(), name = 'all-borrowed'),
		url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
		

]