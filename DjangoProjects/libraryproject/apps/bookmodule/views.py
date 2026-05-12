from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render 
from .models import Book
from django.db.models import Q, F, FloatField, ExpressionWrapper, Count, Avg, Min, Max, Sum
from .models import Book, Publisher, Author, Address, Student
# Create your views here.

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def links_page(request):
    return render(request, 'bookmodule/links.html')
def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')
def listing_page(request):
    return render(request, 'bookmodule/listing.html')
def tables_page(request):
    return render(request, 'bookmodule/tables.html')
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
def simple_query(request):
    mybooks = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books':mybooks})

# ===========================================================
# Task 1: Books with price <= 80 using Q
# ===========================================================
def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})


# ===========================================================
# Task 2: edition > 3 AND (title OR author contains "qu")
# ===========================================================
def lab8_task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})


# ===========================================================
# Task 3: Opposite of Task 2 — using ~ (NOT)
# ===========================================================
def lab8_task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})


# ===========================================================
# Task 4: Order books by title using order_by
# ===========================================================
def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})


# ===========================================================
# Task 5: Aggregation — count, total, avg, max, min
# ===========================================================
def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        average=Avg('price'),
        maximum=Max('price'),
        minimum=Min('price'),
    )
    return render(request, 'bookmodule/stats.html', {'stats': stats})


# ===========================================================
# Task 7: Number of students in each city
# ===========================================================
def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/students_per_city.html', {'cities': cities})



def lab9_task1(request):
    mybooks = Book.objects.annotate(
        percentage=ExpressionWrapper(
            F('quantity') * 100.0 / 350,
            output_field=FloatField()
        )
    )
    return render(request, 'bookmodule/books_with_percentage.html', {'books': mybooks})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/publishers_stock.html', {'publishers': publishers})

def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book=Min('book__pubdate'))
    return render(request, 'bookmodule/publishers_oldest.html', {'publishers': publishers})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price'),
    )
    return render(request, 'bookmodule/publishers_price_stats.html', {'publishers': publishers})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        high_rated_quantity=Sum('book__quantity', filter=Q(book__rating__gte=4)),
    )
    return render(request, 'bookmodule/publishers_high_rated.html', {'publishers': publishers})


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__rating__gte=1)
        )
    )
    return render(request, 'bookmodule/publishers_filtered_count.html', {'publishers': publishers})

def lab10_task1(request):
    mybooks = Book.objects.all().order_by('title')
 
    return render(request, 'bookmodule/lab10_task1.html', {'books': mybooks})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.pubdate = request.POST.get('pubdate')
        book.rating = request.POST.get('rating')

        publisher_id = request.POST.get('publisher')
        book.publisher = Publisher.objects.filter(id=publisher_id).first() if publisher_id else None

        book.save()

        author_ids = request.POST.getlist('authors')
        book.authors.set(Author.objects.filter(id__in=author_ids))

        return redirect('bookmodule:books.lab10_task1')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()

    return render(request, 'bookmodule/edit_book.html', {
        'book': book,
        'publishers': publishers,
        'authors': authors,
    })


def delete_book(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if request.method == 'POST':
        book.delete()
    return redirect('bookmodule:books.lab10_task1')


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        pubdate = request.POST.get('pubdate')
        rating = request.POST.get('rating')
        publisher_id = request.POST.get('publisher')
        author_ids = request.POST.getlist('author')

        publisher = Publisher.objects.get(id=publisher_id) if publisher_id else None

        book = Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            pubdate=pubdate,
            rating=rating,
            publisher=publisher
        )

        if author_ids:
            book.authors.set(Author.objects.filter(id__in=author_ids))

        return redirect('bookmodule:books.lab10_task1')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    return render(request, 'bookmodule/add_book.html', {
        'publishers': publishers,
        'authors': authors
    })