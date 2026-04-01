from . import views
from django.urls import path




urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('html5/links/', views.links_page, name='books.links_page'),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/text/formatting/', views.text_formatting, name='books.text_formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),

]