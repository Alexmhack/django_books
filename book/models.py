from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	year = models.DateField(auto_now_add=True)
	isbn = models.CharField(max_length=13, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	review = models.CharField(max_length=100, help_text='Enter a review for book under 100 words', blank=True)

	RATING = (
		('1', 'Very Good'),
		('2', 'Good'),
		('3', 'Average'),
		('4', 'Bad'),
		('5', 'Very Bad'),
	)

	rating = models.CharField(choices=RATING, help_text='Rate the book on a scale of 1 to 5')
	average = models.DecimalField(help_text='Average review score for book')
