from django.urls import path
from .views import search_book_view,BookRentalHistoryView,UpdateRentalStatusView,CreateNewRentalView
app_name= 'rentals'

urlpatterns = [
    path('',search_book_view,name='main'),
    path('<str:book_id>/',BookRentalHistoryView.as_view(),name='detail'),
    path('new/<str:book_id>/',CreateNewRentalView.as_view(),name='new'),
     path('<str:book_id>/<pk>/',UpdateRentalStatusView.as_view(),name='update'),
      
]
