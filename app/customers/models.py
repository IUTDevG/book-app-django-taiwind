from django.db import models
from books.models import Book
from django.utils.text import slugify

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True,blank=True)
    additional_infor = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(default=50)
    books = models.ManyToManyField(Book,blank=True,help_text='livres actuellement loués')
    book_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.username)

    def save(self,*args,**kwargs):
        # print('//////////////////////////////////',username)
        if not self.username:
            username = slugify(f"{self.first_name} {self.last_name}")
            # username = base_username
            # print('//////////////////////////////////',username)
            ex = __class__.objects.filter(username=username).exists()

            while ex:
                i = len(__class__.objects.filter(first_name=self.first_name,last_name=self.last_name))
                username = slugify(f'{self.first_name} {self.last_name} {i+1}')
                ex = __class__.objects.filter(username=username).exists()
            self.username = username
        super().save(*args,**kwargs)