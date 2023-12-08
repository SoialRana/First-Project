from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)
    publication_date=models.DateField(null=True,auto_now_add=True)
    genre=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class BookInstance(models.Model):
    id=models.IntegerField(primary_key=True)
    book=models.ForeignKey(Book, on_delete=models.CASCADE,null=True)
    book_number=models.PositiveIntegerField(null=True)
    Is_borrowed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id} {self.book}"

class Students(models.Model):
    roll_number = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    def __str__(self):
        return self.fullname
    


class Book_Issue(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)
    remarks_on_issue = models.CharField(max_length=100)
    remarks_on_return = models.CharField(max_length=100)


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    class Meta:
        ordering = ['-borrowed_date']


# class Wishlist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     books = models.ManyToManyField('Book', blank=True)

#     def __str__(self):
#         return self.user.username + "'s Wishlist"
    
    
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review by {self.user.username} for {self.book.title}"
    
    
