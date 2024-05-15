from django.contrib import admin
from myadmin.models import Category, SubCategory, Product
from mydjapp.models import Register
from user.models import Payment

# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display =('p_id','p_title','subcatname','p_description','p_bprice','p_iconname','info','image')
    
admin.site.register(Product, ProductAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'city', 'gender', 'status', 'role', 'info')

    
admin.site.register(Register, RegisterAdmin)    


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('txnid', 'uid', 'amt', 'info')

admin.site.register(Payment, PaymentAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcatname', 'catname', 'subcaticonname')

admin.site.register(SubCategory, SubCategoryAdmin)