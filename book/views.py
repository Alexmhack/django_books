from django.shortcuts import render
from django.views import generic, View

from .models import Book

class BookListView(generic.ListView):
	model = Book
	paginate_by = 10


class BookDetailView(generic.DetailView):
	model = Book


class IndexView(View):
	def get(self, request, *args, **kwargs):
		queryset = Book.objects.all()
		context = {
			'total_count': queryset.count(),
			'book_after_2000': queryset.filter(year__gte=2000).count(),
			'book_before_2000': queryset.filter(year__lte=2000).count(),
			'book_before_1990': queryset.filter(year__lte=1990).count(),
			'book_after_1990': queryset.filter(year__gte=1990).count(),
			'book_after_1980': queryset.filter(year__gte=1980).count(),
			'book_before_1980': queryset.filter(year__lte=1980).count(),
		}
		return render(request, 'book/index.html', context)
