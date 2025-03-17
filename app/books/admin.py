from django.contrib import admin
from .models import Book,BookTitle
# inport export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

# Register your models here.
class BookRessource(resources.ModelResource):
    title = Field()
    status = Field()
    publisher = Field()
   
    class Meta:
        model = Book
        fields = ('title','publisher','isbn','qr_code','status')
        export_order = fields
    def dehydrate_title(self,obj):
        return obj.title.title
    
    def dehydrate_status(self,obj):
        return obj.status
    
    def dehydrate_publisher(self,obj):
        return obj.title.publisher.name

class BookAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = BookRessource
admin.site.register(Book,BookAdmin)
admin.site.register(BookTitle)
