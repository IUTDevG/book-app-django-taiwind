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
        {'first_name': 'Elodie', 'last_name': 'Fournier'},
        {'first_name': 'Lucas', 'last_name': 'Dufresne'},
        {'first_name': 'Camille', 'last_name': 'Leroy'},
        {'first_name': 'Julien', 'last_name': 'Rousseau'},
        {'first_name': 'Manon', 'last_name': 'Blanchard'},
        {'first_name': 'Arthur', 'last_name': 'Fontaine'},
        {'first_name': 'Eva', 'last_name': 'Morin'},
        {'first_name': 'Hugo', 'last_name': 'Chauvet'},
        {'first_name': 'Emma', 'last_name': 'Perrin'},
        {'first_name': 'Nathan', 'last_name': 'Gautier'},
        {'first_name': 'Clara', 'last_name': 'Bernard'}
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
        'Oscar Wilde', 'Edgar Allan Poe', 'Ray Bradbury', 'Philip K. Dick', 'Isaac Asimov',
        'Arthur Conan Doyle', 'Shakespeare', 'Bram Stoker', 'H.P. Lovecraft', 'J.R.R. Tolkien',
        'Jules Renard', 'Stendhal', 'Emile Zola', 'Maurice Leblanc', 'Jean-Paul Sartre'
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
        {'name': 'Actes Sud', 'country': Country('FR')},
        {'name': 'Flammarion', 'country': Country('FR')},
        {'name': 'Bayard', 'country': Country('FR')},
        {'name': 'Les Éditions de Minuit', 'country': Country('FR')},
        {'name': 'Hatier', 'country': Country('FR')},
        {'name': 'Folio', 'country': Country('FR')},
        {'name': 'Le Livre de Poche', 'country': Country('FR')},
        {'name': 'Éditions Soleil', 'country': Country('FR')},
        {'name': 'Glénat', 'country': Country('FR')},
        {'name': 'Casterman', 'country': Country('FR')},
        {'name': 'Delcourt', 'country': Country('FR')}
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

        'L’Odyssée', 'La Divine Comédie', 'Le Rouge et le Noir', 'Les Misérables', 'L’Île au trésor', 'Les Hauts de Hurlevent',
        'La Chartreuse de Parme', 'Le Nom de la Rose', 'Le Meilleur des Mondes', 'L’Assommoir', 'L’Attrape-Cœurs', 
        'Le Comte de Monte-Cristo', 'Le Petit Prince', 'Les Trois Mousquetaires', 'Le Seigneur des Anneaux', 'Les Fleurs du Mal',
        'L’Écume des jours', 'Le Tour du monde en 80 jours', 'Les Aventures de Sherlock Holmes', 'L’Alchimiste', 

        'À la recherche du temps perdu', 'Candide', 'Don Quichotte', 'Éducation sentimentale', 'Fondation', 'Germinal',
        'Histoires extraordinaires', 'Inferno', 'Jonathan Livingston le goéland', 'Kafka sur le rivage', 'L’ombre du vent', 
        'Moby Dick', 'Ne tirez pas sur l’oiseau moqueur', 'Othello', 'Peter Pan', 'Que ma joie demeure', 'Robinson Crusoé', 
        'Sherlock Holmes : Le Chien des Baskerville', 'Treasure Island', 'Ubu Roi', 'Voyage au centre de la Terre', 
        'Wuthering Heights', 'X-Men : Days of Future Past', 'Yellowface', 'Zola : Germinal',

        'Astérix le Gaulois', 'Bourreau des cœurs', 'Cyrano de Bergerac', 'Dix petits nègres', 'Étoiles filantes', 'Fahrenheit 451',
        'Guerre et Paix', 'Harry Potter et la Chambre des Secrets', 'Indiana', 'Jack et le haricot magique', 'Kim', 'L’Illiade',
        'Mort à crédit', 'Narnia : Le Lion, la Sorcière Blanche et l’Armoire magique', 'Oliver Twist', 'Petit Pays',
        'Quo Vadis', 'Réparer les vivants', 'Sous le soleil de Satan', 'Tintin et les Picaros', 'Une vie', 'Voyage en Occident',
        'Water for Elephants', 'X-Files : Les Dossiers Secrets', 'Yoko Tsuno', 'Zazie dans le métro',

        'L’Homme invisible', 'La Horde du Contrevent', 'Le Parfum', 'Les Cavaliers', 'La Nuit des temps', 'Le Clan des Otori',
        'L’Étranger', 'Le Livre sans nom', 'Le Passeur', 'La Vague', 'Les Âmes vagabondes', 'Le Dernier Jour d’un condamné',
        'L’Enfant Noir', 'L’Invention de Morel', 'La Métamorphose', 'Le Rivage des Syrtes', 'L’Œuvre au noir', 
        'La Nuit des enfants rois', 'L’Ami retrouvé', 'La Peste', 'Le Parfum de la Dame en Noir', 'Les Rivières Pourpres', 
        'La Prophétie des Andes', 'Le Silence des agneaux', 'Les Piliers de la Terre',

        'American Gods', 'Baudelaire : Les Paradis artificiels', 'Cosmos', 'Dragon Rouge', 'Énigme de la chambre 622', 
        'Fondation et Empire', 'Génie des Alpages', 'Hunger Games', 'I, Robot', 'Je suis une légende', 'Koh-Lanta : L’aventure',
        'Le Grand Meaulnes', 'Magie vaudou', 'Neige', 'Ombres mouvantes', 'Pierre et Jean', 'Quand sort la recluse', 
        'Ravage', 'Shutter Island', 'Trois jours et une vie', 'Une histoire de France', 'Vers l’infini et au-delà',
        'Winnie l’ourson', 'Xanadu', 'Y : Le dernier homme', 'Zombillénium',

        'Atlas Shrugged', 'Bartleby, le scribe', 'Chroniques martiennes', 'Dracula', 'Éloge de la folie', 'Frère d’âme', 
        'Gide : Les Faux-Monnayeurs', 'Hannibal Lecter', 'Iliade', 'J’accuse !', 'Kirikou et la Sorcière', 'L’Art de la guerre',
        'Manon Lescaut', 'Nos étoiles contraires', 'Orson Welles : Citizen Kane', 'Pensées de Pascal', 'Qui a tué Roger Rabbit ?',
        'Rimbaud : Une saison en enfer', 'Sous les vents de Neptune', 'Tous les hommes du roi', 'Uchronia', 'Vagabond des étoiles',
        'Wild : Marcher pour se retrouver', 'Xerxès', 'Yasmina Khadra : Ce que le jour doit à la nuit', 'Zweig : La Confusion des sentiments'
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
                for book_title in book_titles:
                    quantity = random.randint(1, 5)
                    for _ in range(quantity):
                        Book.objects.create(title=book_title)
                        print(f"Exemplaire ajouté pour : {book_title.title}")

            except Exception as e:
                print(f"Erreur : {e}")
        print('#######################-->creation book fin<--#######################')
        

        # customers
        # customers_list = [
        #     {'first_name':'John','last_name':'Doe'},
        #       {'first_name':'Adman','last_name':'Jones'},
        #         {'first_name':'Toto','last_name':'Dan'}

        # ]
       

    