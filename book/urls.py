from django.urls import path

from .views import (
	BookListView,
	BookDetailView,
)

urlpatterns = [
	path('list/', BookListView.as_view(), name='book-list'),
	path('<int:id>/detail/', BookDetailView.as_view(), name='book-detail'),
]
