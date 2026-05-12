from . import views
from django.urls import path


app_name = 'bookmodule'   # ← this line is required

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.simple_query, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('html5/links/', views.links_page, name='books.links_page'),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/text/formatting/', views.text_formatting, name='books.text_formatting'),
    path('html5/listing/', views.listing_page, name='books.listing'),
    path('html5/tables/', views.tables_page, name='books.tables_page'),
    path('search/', views.search, name='books.search'),
    path('lab8/task1', views.lab8_task1, name='books.lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='books.lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='books.lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='books.lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='books.lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='books.lab8_task7'),
    path('lab9/task1', views.lab9_task1, name='books.lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='books.lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='books.lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='books.lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='books.lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='books.lab9_task6'),
    path('lab10/task1/listbooks', views.lab10_task1, name='books.lab10_task1'),
    path('edit/<int:book_id>/', views.edit_book, name='books.edit'),
    path('delete/<int:book_id>/', views.delete_book, name='books.delete'),
    path('add/', views.add_book, name='books.add'),

]