from django.core.management.base import BaseCommand
from authors.models import Author
from publisher.models import Publisher
from books.models import BookTitle,Book
from customers.models import Customer
from django_countries.fields import Country
import random



class Command(BaseCommand):
    help = 'testing'

    def handle(self, *args, **options):
        # return super().handle(*args, **options)

        #authos
        authors_list = ['John Smith','Adman Jones','John Tom','Jane Johnson']
        for name in authors_list:
            Author.objects.create(name=name)
        # publishers
        publishers_list = [
            {'name':'X books','country':Country(code='fr')},
              {'name':'XY books','country':Country(code='cm')},
                {'name':'Mexte books','country':Country(code='us')}
        ]
        for item in publishers_list:
            Publisher.objects.create(**item)

        # book title
        book_title_list = ['Harry zooter','Lrd of kigth','Django rf','DRF']
        publishers = [x.name for x in Publisher.objects.all()]
        items = zip(book_title_list,publishers)

        for item in items:
            author = Author.objects.order_by('?')[0]
            publisher = Publisher.objects.get(name=item[1])
            BookTitle.objects.create(title=item[0],publisher=publisher,author=author)
        # book
        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        # customers
        customers_list = [
            {'first_name':'John','last_name':'Doe'},
              {'first_name':'Adman','last_name':'Jones'},
                {'first_name':'Toto','last_name':'Dan'}

        ]
        for item in customers_list:
            Customer.objects.create(**item)
    