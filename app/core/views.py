from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView
from django.db.models import Count,Sum
from books.models import BookTitle,Book
from rentals.models import Rental
from rentals.choices import STATUS_CHOICES
from customers.models import Customer
from publisher.models import Publisher


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

# def chart_data(request):
#     data = []
#     # book titles vs books (bar)
#     all_books = len(Book.objects.all())
#     all_book_titles = len(BookTitle.objects.all())
#     print('>>>>>>>>>>>>>>>>>>.')
#     data.append({
#         'labels':['books','book titles'],
#         'data':[all_books,all_book_titles],
#         'description':'unique book titles vs books',
#         'type':'bar',
#     })
#     print(data)
#     # book title count by publisher (pie)
#     titles_by_publisher = BookTitle.objects.values('publisher__name').annotate(Count('publisher__name'))
#     print(titles_by_publisher)
#     publisher_names = [x['publisher__name'] for x in titles_by_publisher]
#     publisher_names_count = [x['publisher__name__count'] for x in titles_by_publisher]
#     data.append({
#         'labels':publisher_names,
#         'data':publisher_names_count,
#         'description':'book title count by publisher',
#         'type':'pie',
#     })
#     # books by status (pie)
#     book_by_status = Rental.objects.values('status').annotate(Count('book_title'))
#     book_title_count = [x['book__title'] for x in book_by_status]
#     status_keys = [x['status'] for x in book_by_status]
#     status = [dict(STATUS_CHOICES)[key] for key in status_keys ]
#     data.append({
#         'labels':status,
#         'data':book_title_count,
#         'description':'book by status',
#         'type':'pie'
#     })

#     # publishers vs customers (bar)
#     customers = len(Customer.objects.all())
#     publishers = len(Publisher.objects.all())
#     data.append({
#         'labels': ['customers', 'publishers'],
#         'data': [customers, publishers],
#         'description': 'customers vs publishers',
#         'type' : 'bar'
#     })
#     # qs = BookTitle.objects.aggregate(Count('publishier'))
#     return JsonResponse({'data':data})

def chart_data(request):

    # if not is_ajax(request):
    #     return redirect('home')

    data = []
    # 1) book titles vs books (bar)
    all_books = len(Book.objects.all())
    all_book_titles = len(BookTitle.objects.all())
    data.append({
        'labels': ['books', 'book titles'],
        'data': [all_books, all_book_titles],
        'description': 'unique book titles vs books',
        'type': 'bar',
    })
    # 2) book title count by publisher (pie)
    titles_by_publisher = BookTitle.objects.values('publisher__name').annotate(Count('publisher__name'))
    publisher_names = [x['publisher__name'] for x in titles_by_publisher]
    publisher_names_count = [x['publisher__name__count'] for x in titles_by_publisher]
    data.append({
        'labels': publisher_names,
        'data': publisher_names_count,
        'description': 'book title count by publisher',
        'type': 'pie',
    })

    # 3) books by status (pie)
    book_by_status = Rental.objects.values('status').annotate(Count('book__title'))
    book_title_count = [x['book__title__count'] for x in book_by_status]
    status_keys = [x['status'] for x in book_by_status]
    status = [dict(STATUS_CHOICES)[key] for key in status_keys]
    data.append({
        'labels': status,
        'data': book_title_count,
        'description': 'book by status',
        'type': 'pie'
    })

    # 4) publishers vs customers (bar)
    customers = len(Customer.objects.all())
    publishers = len(Publisher.objects.all())
    data.append({
        'labels': ['customers', 'publishers'],
        'data': [customers, publishers],
        'description': 'customers vs publishers',
        'type' : 'bar'
    })

    print(data)

    return JsonResponse({'data': data})


def change_theme(request):
    if 'is_dark_mode' in request.session:
         request.session['is_dark_mode'] = not  request.session['is_dark_mode'] 
        
    else:
        request.session['is_dark_mode'] = False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request):
    return render(request,'main.html')
