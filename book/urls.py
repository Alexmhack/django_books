from django.urls import path

from .views import BookListView

urlpatterns = [
	path('list/', BookListView, name='book-list'),
]
