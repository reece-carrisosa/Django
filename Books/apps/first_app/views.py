from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    # Book.objects.create(title="Holes", author="Louis Sachar", category="Fiction")
    # Book.objects.create(title="Grumpy Gills", author="Jamal Kukit", category="Non Fiction")
    # Book.objects.create(title="We All We Got", author="Omar Landeros", category="Fiction")
    # Book.objects.create(title="Tomorrow's Never Promised", author="Gayle McDough", category="SciFi")
    # Book.objects.create(title="Be Humble", author="Samantha Ravel", category="Fiction")
    book = Book.objects.all()
    for val in book:
        print 'Book Title:', val.title
        print 'Book Author:', val.author
        print 'Published Date:', val.publishedDate
        print 'Category:', val.category
    return render(request, "first_app/index.html")