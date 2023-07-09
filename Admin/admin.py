from django.contrib import admin
from .models import Category,Product,Recent,PaymentMaster

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","Category_name")

class Product_Admin(admin.ModelAdmin):
    list_display = ("id", "pname","price","description",
       "size","quantity","image","cat")
class Recent_Update(admin.ModelAdmin):
    list_display = ("image",)

class PaymentMaster_Admin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","ballance")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, Product_Admin)
admin.site.register(Recent, Recent_Update)
admin.site.register(PaymentMaster,PaymentMaster_Admin)