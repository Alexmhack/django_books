from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse

from book.models import Book
from .forms import JsonDataForm

class BookAPIView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'api/index.html')


class BookAPIFormView(View):
	def get(self, request, *args, **kwargs):
		form = JsonDataForm()
		context = {
			'form': form
		}
		return render(request, 'api/json_form.html', context)

	def post(self, request, *args, **kwargs):
		form = JsonDataForm(request.POST)
		context = {
			'form': form
		}
		template = "api/json_form.html"
		if form.is_valid():
			template = "api/json_data_success.html"
			isbn_value = form.cleaned_data.get('isbn')
			book = Book.objects.get(isbn=isbn_value)
			context = {
				'book': book
			}
		return render(request, template, context)


class BookAPIJson(View):
	def get(self, request, *args, **kwargs):
		isbn = kwargs.get('isbn', '')
		isbn_value = str(isbn)
		if len(isbn_value) == 9:
			isbn_value += '0'
		book = get_object_or_404(Book, isbn=isbn_value)
		data = {
			"title": book.title,
			"author": book.author,
			"year": book.year,
			"isbn": book.isbn,
			"review_count": 28,
			"average_score": 5.0
		}
		return JsonResponse(data)
