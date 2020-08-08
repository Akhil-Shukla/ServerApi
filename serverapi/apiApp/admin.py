from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Users)
admin.site.register(Store)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Brands)
admin.site.register(UserCart)
