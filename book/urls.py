from django.urls import path

from .views import (
	BookListView,
	BookDetailView,
	IndexView,
	SearchFormResultsView,
)

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('list/', BookListView.as_view(), name='book-list'),
	path('<int:pk>/detail/', BookDetailView.as_view(), name='book-detail'),
	path('search-results/', SearchFormResultsView.as_view(), name='search-results'),
]
