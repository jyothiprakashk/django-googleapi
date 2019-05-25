import requests
from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

def index(request):
        url = 'https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyBN1EB3WWf24C-9OF3I9f8mDGEhZ7WPVY4'
        if request.method=='POST':
            form = BookForm(request.POST)
            form.save()
        form = BookForm()
        books = Book.objects.all()
        

        book_data =[]
        for book in books:
            r= requests.get(url.format(book)).json()
            book_Api = {
                'id': book.id,
                'title' : r['items'][0]['volumeInfo']['title'],
                'author' : r['items'][0]['volumeInfo']['authors'],
                'publishdate' : r['items'][0]['volumeInfo']['publishedDate'],
                'description' : r['items'][0]['volumeInfo']['description'],
                'icon' : r['items'][0]['volumeInfo']['imageLinks']['thumbnail'],
                'infoLink' :r['items'][0]['volumeInfo']['infoLink'],
            }
           
            book_data.append(book_Api)
            
           
            
        context = {'book_data' : book_data, 'form' : form}

        return render(request, 'BookApi/book.html',context) 
def delete(request, id):
    
    if request.method == 'POST':
        Book.objects.filter(id=id).delete()

    return redirect('/')





