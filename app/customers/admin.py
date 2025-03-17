from django.contrib import admin
from .models import Customer
# inport export
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
# Register your models here.
class CustomerRessource(resources.ModelResource):
    additional_infor = Field()
    books = Field()
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name','username','additional_infor','rating','books','book_count')
        export_order = fields

class CustomerAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = CustomerRessource
    def dehydrate_additional_infor(self,obj):
       if len(obj.additional_infor) == 0:
           return "-"
       elif len(obj.additional_infor) < 5:
           return obj.additional_infor
       else:
           txt_list = obj.additional_infor.split(" ")[:5]
           return " ".join(txt_list) + "..."
       
    def dehydrate_books(self,obj):
        books = [x.isbn for x in obj.books.all()]
        return ", ".join(books)

admin.site.register(Customer,CustomerAdmin)
