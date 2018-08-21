from django.urls import path

from .views import BookListView

urlpatterns = [
	path('list/', BookListView.as_view(), name='book-list'),
]
