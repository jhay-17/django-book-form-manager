from django.contrib import admin  
from django.urls import path
from crudapp import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('bookrecords/', views.bookrecords, name="bookrecords"),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]