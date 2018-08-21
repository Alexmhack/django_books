from django.shortcuts import render
from django.views import View

from book.models import Book

class BookAPIView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'api/index.html')
