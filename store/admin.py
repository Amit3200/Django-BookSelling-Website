from django.contrib import admin
from .models import Book,Author,BookOrder,Cart
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','price','stock')

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name')

class BookOrderAdmin(admin.ModelAdmin):
    list_display=('book','cart','quantity')

class CartAdmin(admin.ModelAdmin):
    list_display=('user','active','order_date')


admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookOrder,BookOrderAdmin)
admin.site.register(Cart,CartAdmin)