from django.urls import path

from .views import (
	BookListView,
	BookDetailView,
	IndexView,
)

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('list/', BookListView.as_view(), name='book-list'),
	path('<int:id>/detail/', BookDetailView.as_view(), name='book-detail'),
]
