from django import forms 
from book.models import Book,BookInstance,Students,Book_Issue

class BookStoreForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['id','title','author','isbn']
        
        
class Book_instanceForm(forms.ModelForm):
    class Meta:
        model=BookInstance
        fields = ['book','book_number']
        
        
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        
        
class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=Book_Issue
        exclude = ['issue_date','remarks_on_return',]