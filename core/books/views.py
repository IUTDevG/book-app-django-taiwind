from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView,FormView
from .forms import BookTitleForm
from django.urls import reverse, reverse_lazy

# Create your views here.
class BookTitleView(FormView,ListView):
    # model = BookTitle
    template_name = 'books/main.html'
    context_object_name = 'book_titles'
    form_class = BookTitleForm
    # success_url = reverse_lazy('books:main')

    def get_success_url(self):
        return self.request.path


    def get_queryset(self):
        parameter = 'l'
        return BookTitle.objects.filter(title__startswith=parameter)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        return super().form_invalid(form)
        
    

# def book_title_list_view(request):
#     qs = BookTitle.objects.all()
#     return render(request,'books/main.html',{'qs':qs})
