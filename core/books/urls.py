from django.urls import path
from .views import BookTitleView
app_name ='books'

urlpatterns=[
      path('',BookTitleView.as_view(),name='main'),
    # path('<pk>',book_title_detail_view),
]