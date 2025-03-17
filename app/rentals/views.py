from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import SearchBookForm
from books.models import Book
from .models import Rental
from django.views.generic import ListView,UpdateView,CreateView
from django.db.models import Q
from datetime import datetime
from django.contrib import messages

# Create your views here.
def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query = request.POST.get('search', None)
    book_ex = Book.objects.filter(Q(id=search_query)|Q(isbn=search_query)).exists()

    if search_query is not None and book_ex:
        return redirect('rentals:detail',search_query)
    context = {'form':form}

    return render(request,'rentals/main.html',context)

class BookRentalHistoryView(ListView):
    model = Rental
    template_name = 'rentals/detail.html'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')

        return Rental.objects.filter(Q(book__id=book_id)|Q(book__isbn=book_id))
    

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        # qs =  self.get_queryset()
        # obj = Book.objects.filter(id=book_id).first()
        obj = get_object_or_404(Book,Q(id=book_id)|Q(isbn=book_id))
        # if qs.exists():
        #     obj = qs.first()
        context['object'] = obj

        return context

class UpdateRentalStatusView(UpdateView):
    model = Rental
    template_name = 'rentals/update.html'
    fields = ('status',)

    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail',kwargs={'book_id':book_id})
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.status == '#1':
            instance.rent_date = datetime.today().date()
            instance.is_closed = True
        instance.save()
        messages.add_message(self.request,messages.INFO,f"{instance.book.id} was successfuly updated")
        return super().form_valid(form)

class CreateNewRentalView(CreateView):
    model = Rental
    template_name = 'rentals/new.html'
    fields = ('customer',)
    
    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail',kwargs={'book_id':book_id})
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        book_id = self.kwargs.get('book_id')
        obj = Book.objects.get(id=book_id)
        instance.book = obj
        instance.status = '#0'
        instance.rent_start_date = datetime.today().date()
        instance.save()
        return super().form_valid(form)
    
