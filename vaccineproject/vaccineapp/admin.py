from django.contrib import admin
from .models import People,District,Taluk,Vaccine

# Register your models here.
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(People)
admin.site.register(Vaccine)