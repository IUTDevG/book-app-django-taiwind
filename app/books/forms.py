from django import forms
from .models import BookTitle
from django.core.exceptions import ValidationError

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('publisher','author','title')
        # widgets={
        #     'title':forms.TextInput(attrs={'class':'border bg-purple-200 p-3 rounded-xl'}),
        #      'author':forms.Select(attrs={'class':'border bg-purple-200 p-3 rounded-xl'}),
        #       'publisher':forms.Select(attrs={'class':'border bg-purple-200 p-3 rounded-xl'})
        # }

    def clean(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
            error_msg = 'the title is too short'
            # raise ValidationError(error_msg)
            self.add_error('title','the title is too short')
        
        book_title_exists = BookTitle.objects.filter(title__iexact=title).exists()
        if book_title_exists:
            # error_msg_existy = "this book title already existy"

            # raise ValidationError(error_msg_existy)
            self.add_error('this book title already existy')
        return self.cleaned_data
