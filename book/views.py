from django.shortcuts import render
from django.views import generic, View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .models import Book
from .forms import JsonDataForm

class BookListView(generic.ListView):
	model = Book
	paginate_by = 9
	ordering = ['-year']

	def get_context_data(self, *args, **kwargs):
		queryset = super().get_context_data()
		book_list = Book.objects.all()
		paginator = Paginator(book_list, 25)
		page = self.request.GET.get('page')
		try:
			book_page = paginator.page(page)
		except PageNotAnInteger:
			book_page = paginator.page(1)
		except EmptyPage:
			book_page = paginator.page(paginator.num_pages)

		queryset['book_page'] = book_page
		return queryset


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


class SearchFormResultsView(View):
	def post(self, request, *args, **kwargs):
		query = request.POST.get('query')
		query = str(query)
		int_query = 0
		try:
			int_query = int(query)
		except Exception as e:
			int_query = query
		context = {'query': query}
		try:
			books = Book.objects.filter(
				Q(title__contains=query) |
				Q(author__contains=query) |
				Q(year__contains=int_query) |
				Q(isbn__contains=int_query)
			)
			print(books)
			if len(books) == 0:
				context['no_results'] = "No results found"
			context['books'] = books
			context['search_results'] = books.count()
			context['string'] = "result" if books.count() == 1 else "results"
		except Exception as e:
			context['error'] = e
			print(e)
		return render(request, 'book/search_results.html', context)
