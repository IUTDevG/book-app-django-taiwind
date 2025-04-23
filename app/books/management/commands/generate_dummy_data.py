from django.core.management.base import BaseCommand
from authors.models import Author
from publisher.models import Publisher
from books.models import BookTitle,Book
from customers.models import Customer
from django_countries.fields import Country
import random


# class Command(BaseCommand):

#     help = "generate dummy data for testing purposes"

#     def handle(self, *args, **kwargs):
#         # generating authors
#         print("generating dummy data...")

#         authors_list = ['John Smith', 'Adam Jones', 'Jane Johnson', 'Megan Tyler']
#         for name in authors_list:
#             Author.objects.create(name=name)

#         # generating publishers
#         print("generating publishers")
#         publishers_list = [
#             {'name': 'X books', 'country': Country(code='us')},
#             {'name': 'Bookz', 'country': Country(code='de')},
#             {'name': 'Edu Mind', 'country': Country(code='gb')},
#             {'name': 'Next', 'country': Country(code='pl')},
#         ]

#         for item in publishers_list:
#             Publisher.objects.create(**item)

#         # generating book titles
#         print("generating book titles")
#         book_titles_list = ['Harry Zotter', 'Lord of the Wings', 'Django Made Easy', 'Switcher']
#         publishers = [x.name for x in Publisher.objects.all()]
#         items = zip(book_titles_list, publishers)

#         for item in items:
#             author = Author.objects.order_by('?')[0]
#             publisher = Publisher.objects.get(name=item[1])
#             BookTitle.objects.create(title=item[0], publisher=publisher, author=author)

#         # generating books
#         print("generating books")
#         book_titles = BookTitle.objects.all()
#         for title in book_titles:
#             quantity = random.randint(1,5)
#             for i in range(quantity):
#                 Book.objects.create(title=title)

#         # generating customers
#         print("generating customers")
#         customers_list = [
#             {'first_name': 'John', 'last_name': 'Doe'},
#             {'first_name': 'Adam', 'last_name': 'Harris'},
#             {'first_name': 'Lisa', 'last_name': 'Martinez'},
#         ]

#         for item in customers_list:
#             Customer.objects.create(**item)
            
    

class Command(BaseCommand):
    help = 'testing'

    def handle(self, *args, **options):
        # return super().handle(*args, **options)
        customers_list = [
        {'first_name': 'Alice', 'last_name': 'Dupont'},
        {'first_name': 'Michel', 'last_name': 'Bertrand'},
        {'first_name': 'Sophie', 'last_name': 'Lemoine'},
        {'first_name': 'Thomas', 'last_name': 'Durand'},
        {'first_name': 'Isabelle', 'last_name': 'Moreau'},
        {'first_name': 'Nicolas', 'last_name': 'Girard'},
        {'first_name': 'Claire', 'last_name': 'Robert'},
        {'first_name': 'Jean', 'last_name': 'Marchand'},
        {'first_name': 'Paul', 'last_name': 'Lambert'},
     
        ]

        for item in customers_list:
            Customer.objects.create(**item)
        print('#######################-->creation customers fin<--#######################')

        #authos
        # authors_list = ['John Smith','Adman Jones','John Tom','Jane Johnson']
        authors_list = [
        'Victor Hugo', 'Jane Austen', 'J.K. Rowling', 'Stephen King', 'Agatha Christie',
        'George Orwell', 'Ernest Hemingway', 'Mark Twain', 'Jules Verne', 'Leo Tolstoy',
        'Alexandre Dumas', 'Gustave Flaubert', 'Honoré de Balzac', 'Charles Dickens', 'Franz Kafka',
        'Albert Camus', 'Fyodor Dostoevsky', 'Haruki Murakami', 'Margaret Atwood', 'Gabriel García Márquez',
        'Oscar Wilde', 'Edgar Allan Poe'
        ]

        for name in authors_list:
            try:
            
                Author.objects.create(name=name)
            except:
                continue
        print('#######################-->creation authors fin<--#######################')
        # publishers
        publishers_list = [
            {'name':'X books','country':Country(code='fr')},
              {'name':'XY books','country':Country(code='cm')},
                {'name':'Mexte books','country':Country(code='us')}
        ]
        publishers_list = [
        {'name': 'Gallimard', 'country': Country('FR')},
        {'name': 'Penguin Random House', 'country': Country('US')},
        {'name': 'HarperCollins', 'country': Country('US')},
        {'name': 'Hachette Livre', 'country': Country('FR')},
        {'name': 'Macmillan Publishers', 'country': Country('GB')},
        {'name': 'Simon & Schuster', 'country': Country('US')},
        {'name': 'Scholastic', 'country': Country('US')},
        {'name': 'Albin Michel', 'country': Country('FR')},
        {'name': 'Seuil', 'country': Country('FR')},
      
        ]


        for item in publishers_list:
            Publisher.objects.create(**item)
        print('#######################-->creation publisher fin<--#######################')
        # book title
        # book_title_list = ['Harry zooter','Lrd of kigth','Django rf','DRF']
        book_title_list = [
        'Alice au pays des merveilles', 'Bel-Ami', 'Crime et Châtiment', 'Dune', 'Emma', 'Frankenstein', 'Gatsby le Magnifique',
        'Hamlet', 'Illusions perdues', 'Jane Eyre', 'King Lear', 'L’étranger', 'Madame Bovary', 'Notre-Dame de Paris',
        'Orgueil et Préjugés', 'Persuasion', 'Quatrevingt-treize', 'Roméo et Juliette', 'Shining', 'Tintin au Tibet',
        'Ulysse', 'Vingt Mille Lieues sous les Mers', 'War and Peace', 'Xénophon : Anabase', 'Yvain, le chevalier au lion', 'Zadig',
    ]

        # publishers = [x.name for x in Publisher.objects.all()]
        # items = zip(book_title_list,publishers)

        # for item in items:
        #     author = Author.objects.order_by('?')[0]
        #     publisher = Publisher.objects.get(name=item[1])
        #     try:
        #         BookTitle.objects.create(title=item[0],publisher=publisher,author=author)
        #         print(f"{BookTitle.objects.create(title=item[0],publisher=publisher,author=author)}")
        #     except:
        #         continue
        # # book
        # book_titles = BookTitle.objects.all()
        # for title in book_titles:
        #     quantity = random.randint(1,5)
        #     for i in range(quantity):
        #         Book.objects.create(title=title)
        publishers_list = list(Publisher.objects.all())  # Récupère les objets au lieu des noms
        if not publishers_list:
            print("Aucun éditeur trouvé !")
            return

        for title in book_title_list:
            publisher = random.choice(publishers_list)
            author = Author.objects.order_by('?').first()

            try:
                book = BookTitle.objects.create(title=title, publisher=publisher, author=author)
                print(f"Livre ajouté : {book.title}")
                book_titles = BookTitle.objects.all()
                                # book_titles = BookTitle.objects.all()
               

            except Exception as e:
                print(f"Erreur : {e}")
        for book_title in book_titles:
                quantity = random.randint(1, 5)
                for _ in range(quantity):
                    Book.objects.create(title=book_title)
                    print(f"Exemplaire ajouté pour : {book_title.title}")
        print('#######################-->creation book fin<--#######################')
        

        # customers
        # customers_list = [
        #     {'first_name':'John','last_name':'Doe'},
        #       {'first_name':'Adman','last_name':'Jones'},
        #         {'first_name':'Toto','last_name':'Dan'}

        # ]
       

    