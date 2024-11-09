from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    
    def __str__(self): 
        return "%s" %(self.isbn)
    class Meta:
        db_table = "book" 