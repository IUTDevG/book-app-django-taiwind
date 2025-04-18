from django.urls import path
from .views import( BookTitleView,BookTitleDetailView,BookDetailView,BookDeleteView)
app_name ='books'

urlpatterns=[
    path('',BookTitleView.as_view(),{'letter':None},name='main'),
    path('<str:letter>/',BookTitleView.as_view(),name='main'),
    path('<str:letter>/<slug>/',BookTitleDetailView.as_view(),name='detail'),
    path('<str:letter>/<slug>/<pk>/',BookDetailView.as_view(),name='detail-book'),
    path('<str:letter>/<slug>/<pk>/delete/',BookDeleteView.as_view(),name='delete-book'),
]