import datetime
from django.db import models

current_year = datetime.datetime.now().year

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	year = models.PositiveSmallIntegerField(
		default=current_year,
		help_text='Enter the year YYYY when book was published'
	)
	isbn = models.CharField(
		max_length=10,
		help_text='10 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
	)
