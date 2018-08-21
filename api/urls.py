from django.urls import path

from .views import (
	BookAPIView,
	BookAPIFormView,
)

urlpatterns = [
	path('', BookAPIView.as_view(), name='book-api'),
	path('isbn-form/', BookAPIFormView.as_view(), name='isbn-form'),
]