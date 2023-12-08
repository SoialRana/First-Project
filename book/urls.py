from django.urls import path
from . import views

urlpatterns = [
    path('add_new_student', views.add_new_student, name='add_new_student'),
    path('add_new_book', views.add_new_book, name='add_new_book'),
    path('add_book_issue', views.add_book_issue, name='book_issue'),
    # path('add_new_book_instance', views.add_new_book_instance, name='add_new_book_instance'),
    path('show_students', views.view_students, name='show_student_record'),
    path('view_books', views.view_books, name='view_books'),
    path('view_books_issued', views.view_bissue, name='show_issue_record'),
    path('book_search', views.book_search, name='book_search'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    # path('return/<int:book_id>/', views.return_book, name='return_book'),
    # path('edit_book/<int:id>',views.edit_book,name='edit_book'),
    # path('delete_book/<int:id>',views.delete_book,name='delete_book'),
    # path('edit/student/<str:roll>',views.edit_student_data,name="Edit Student data"),
    # path('edit/book/<uuid:id>',views.edit_book_data,name="Edit Student data"),
    # path('delete/student/<str:roll>',views.delete_student,name="Delete Student data"),
    # path('delete/book/<str:id>',views.delete_book,name="Delete book data"),
    # path('return_book/<int:id>',views.return_issued_book,name="return_issued_book"),
    # path('edit_issued/<int:id>',views.edit_issued,name="edit_issued"),
]
