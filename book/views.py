from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from book.forms import BookStoreForm,Book_instanceForm,StudentsForm,Book_IssueForm
from book.models import Book,BookInstance,Book_Issue,Students,Borrowing
from django.http import HttpResponse

# Create your views here.
def add_new_student(request):
    if request.method=="POST":
        form = StudentsForm((request.POST))
        if form.is_valid():
            form.save()
            return redirect('/show_students')
    else:
        form = StudentsForm
    return (render(request, 'book/add_new_student.html', {'form':form}))



def add_new_book(request):
    if request.method=="POST":
        form = BookStoreForm(request.POST)
        if form.is_valid():
            form=form.save()
            book_instance=BookInstance(book=form)
            book_instance.save()
            return redirect('/view_books')
    else:
        form = BookStoreForm
        form_instance=Book_instanceForm
        return render(request, 'book/add_new_book.html', {'form':form,"form_instance":form_instance})

def view_books(request):
    books=BookInstance.objects.all()
    return render(request,'book/view_books.html', {'books': books})


def add_book_issue(request):
    if request.method=="POST":
        form = Book_IssueForm(request.POST)
        if form.is_valid():
            # save data
            unsaved_form=form.save(commit=False)
            book_to_save=BookInstance.objects.get(id=unsaved_form.book_instance.id)
            book_to_save.Is_borrowed=True
            book_to_save.save()
            form.save()
            form.save_m2m()
        return redirect('/view_books')
    else:
        context={'form':Book_IssueForm,"book":BookInstance.objects.filter(Is_borrowed=False)}
        return render(request, 'book/add_book_issue.html',context=context)


def view_students(request):
    students = Students.objects.order_by('-id')
    return render(request,'book/view_students.html', {'students': students})

def view_books(request):
    books=BookInstance.objects.order_by('id')
    return render(request,'book/view_books.html', {'books': books})

def view_bissue(request):
    issue = Book_Issue.objects.order_by('-id')
    return render(request,'book/issue_records.html', {'issue': issue})

def add_new_book_instance(request):
    form=Book_instanceForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/view_books')

def return_issued_book(request,id):   
    obj=Book_Issue.objects.get(id=id)
    return HttpResponse(f"<h2>Return Issued Book</h2><label>Book <i>{obj.book_instance.book.book_title}</i> issued to <i>{obj.student.fullname}</i> could not be returned..</label>")

def edit_issued(request, id):
    obj=Book_Issue.objects.get(id=id)
    return HttpResponse(f"<h2>Edit Issued Book</h2><label>Book <i>{obj.book_instance.book.book_title}</i> issued to <i>{obj.student.fullname}</i> could not be edited..</label>")


def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.quantity > 0:
        # Create a borrowing record
        Borrowing.objects.create(user=request.user, book=book)

        # Update the book's quantity
        book.quantity -= 1
        book.save()

        # Redirect to a success page or book detail page
        return redirect('view_books', book_id=book.id)
    else:
        # Handle the case when the book is not available
        # You may want to display a message to the user
        return render(request, 'book_not_available.html')


# def return_book(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)

#     # Check if the user has borrowed this book
#     borrowing = Borrowing.objects.filter(user=request.user, book=book, returned=False).first()

#     if borrowing:
#         # Record the return transaction
#         borrowing.returned = True
#         borrowing.save()

#         # Update the book's quantity
#         book.quantity += 1
#         book.save()

#         # Create a book review if desired
#         review_content = request.POST.get('review_content', '')
#         if review_content:
#             Review.objects.create(user=request.user, book=book, content=review_content)

#         # Redirect to a success page or book detail page
#         return redirect('book_detail', book_id=book.id)
#     else:
#         # Handle the case when the user has not borrowed this book
#         # You may want to display a message to the user
#         return render(request, 'book_not_borrowed.html')



def book_search(request):
    query = request.GET.get('q')  # Get the search query from the URL parameter
    books = Book.objects.filter(title__icontains=query) if query else []
    return render(request, 'book_search.html', {'books': books, 'query': query})


# def view_wishlist(request):
#     # Get the user's wishlist
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user)

#     return render(request, 'library/wishlist.html', {'wishlist': wishlist})


# def add_to_wishlist(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user)
#     wishlist.books.add(book)
#     return redirect('view_wishlist')

# def remove_from_wishlist(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     wishlist = Wishlist.objects.get(user=request.user)
#     wishlist.books.remove(book)
#     return redirect('view_wishlist')