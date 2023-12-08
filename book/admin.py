from django.contrib import admin
from .models import Book,Students,Book_Issue,BookInstance,Borrowing
# Register your models here.

admin.site.register(Book)
admin.site.register(Students)
admin.site.register(Book_Issue)
admin.site.register(BookInstance)
admin.site.register(Borrowing)