from django.contrib import admin
from .models import User,Type_menu,Menu,Order_user,Order

admin.site.register(User)
admin.site.register(Type_menu)
admin.site.register(Menu)
admin.site.register(Order_user)
admin.site.register(Order)
