from django.db import models



class BookNumber(models.Model):
    isbn_10             = models.CharField(max_length=10)
    isbn_13             = models.CharField(max_length=13)

class Book(models.Model):
    title               = models.CharField(max_length=36, blank=False, unique=True)
    description         = models.TextField(max_length=256 ,blank=True)
    price               = models.FloatField(default=0)
    published           = models.DateTimeField(auto_now_add=True)
    is_published        = models.BooleanField(default=False)
    cover               = models.ImageField(upload_to='covers/', blank=True, null=True)
    number              = models.OneToOneField(BookNumber, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='character')

class Author(models.Model):
    name = models.CharField(max_length=25)
    books = models.ManyToManyField(Book, related_name='author')