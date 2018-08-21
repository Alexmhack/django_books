from django.shortcuts import render
from django.views import View

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
