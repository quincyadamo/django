from __future__ import unicode_literals
from django.shortcuts import render
from .models import Books

# Create your views here.
def index(request):
    Books.objects.create(title="Harry Potter and the Sorcerers Stone",
    author="J. K. Rowling",
    category="Fantasy",
    published_date="1998-09-01",
    in_print=True)

    Books.objects.create(title="Harry Potter and the Chamber of Secrets",
    author="J. K. Rowling",
    category="Fantasy",
    published_date="1999-06-02",
    in_print=True)

    Books.objects.create(title="Harry Potter and the Prisoner of Azkaban",
    author="J. K. Rowling",
    category="Fantasy",
    published_date="1999-09-08",
    in_print=True)

    Books.objects.create(title="Harry Potter and the Goblet of Fire",
    author="J. K. Rowling",
    category="Fantasy",
    published_date="2000-07-08",
    in_print=True)

    Books.objects.create(title="Harry Potter and the Order of the Phoenix",
    author="J. K. Rowling",
    category="Fantasy",
    published_date="2003-06-21",
    in_print=True)

    books = Books.objects.all()
    print (books)
    return render(request, 'myApp/index.html')
