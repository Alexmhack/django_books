from django.forms import ModelForm

from book.models import Book

class JsonDataForm(ModelForm):
	class Meta:
		model = Book
		fields = ['isbn']
