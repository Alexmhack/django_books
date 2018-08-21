from django.shortcuts import render
from django.views import generic

from .models import Book

class BookListView(generic.ListView):
	model = Book
	paginate_by = 10


class BookDetailView(generic.DetailView):
	model = Book
