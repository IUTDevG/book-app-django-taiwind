from django.shortcuts import render
from django.http import HttpResponseRedirect

def change_theme(request):
    if 'is_dark_mode' in request.session:
         request.session['is_dark_mode'] = not  request.session['is_dark_mode'] 
        
    else:
        request.session['is_dark_mode'] = False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request):
    return render(request,'main.html')
