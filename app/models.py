from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    idno = models.CharField(max_length=100)
    prnno = models.CharField(max_length=100)
    member_type = models.CharField(max_length=50, choices=(
        ('teacher','teacher'),
        ('student','student'),
    ))

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbnno = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=(
        ('technology','technology'),
        ('general','general'),
        ('programming','programming'),
        ('science','science'),
        ('novel','novel'),
    ))
    price = models.FloatField()
    qty = models.IntegerField()

class Loan(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_borrow = models.DateField()
    date_due = models.DateField()
    days_on_books = models.IntegerField()
    
class ReturnBook(models.Model):    
    loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    return_date = models.DateField()
    charges = models.IntegerField()
    dateoverdue = models.CharField(max_length=50, choices=(
        ('yes','yes'),
        ('no','no'),
    ))

