from django.shortcuts import render
from .models import CustomUser
from django.views.generic import ListView, FormView,DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
# Create your views here.

class CustomuserView(LoginRequiredMixin,FormView,ListView):
    template_name = 'users/main.html'
    context_object_name = 'users_list'
    form_class = CustomUserForm
    
    i_instance = None
    
    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        self.i_instance = form.save()
        messages.add_message(self.request,messages.INFO,f"User : {self.i_instance.username} has been create")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.add_message(self.request,messages.ERROR,form.errors)
        return super().form_invalid(form)
        
class CustomuserDeleteView(LoginRequiredMixin,DeleteView):
    model = CustomUser
    template_name = 'books/confirm_delete.html'
    
    def get_success_url(self):
        messages.add_message(self.request,messages.INFO,f"The user with id {self.get_object().id} has been delete")
        return super().get_success_url()
    
