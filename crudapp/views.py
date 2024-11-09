from django.shortcuts import render, redirect
from crudapp.forms import BookForm
from crudapp.forms import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book(request):
    form = BookForm()  # Define form here to ensure it’s available in all cases
    if request.method == "POST":
        form = BookForm(request.POST)  # Update form with POST data if it's a POST request
        if form.is_valid():
            try:
                form.save()
                return redirect('/book')
            except:
                pass
    return render(request, 'bookform.html', {'form': form})

def bookrecords(request):
    books = Book.objects.all()
    return render(request, 'bookrecords.html', {'books': books})

def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST, instance = book)
    if form.is_valid():
        form.save()
        return redirect('/bookrecords')
    else:
        form = BookForm(instance=book)
        return render(request, 'edit_book.html', {'form': form, 'book': book})
    
def delete_book(request, book_id): 
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/bookrecords')