from django.urls import path

from .views import (
	BookAPIView,
	BookAPIFormView,
	BookAPIJson,
)

urlpatterns = [
	path('', BookAPIView.as_view(), name='book-api'),
	path('isbn-form/', BookAPIFormView.as_view(), name='isbn-form'),
	path('<int:isbn>', BookAPIJson.as_view(), name='api-json'),
]