from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	year = models.DateField(auto_now_add=True)
	isbn = models.CharField(max_length=13, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
