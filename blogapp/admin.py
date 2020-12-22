from django.contrib import admin
from .models import profiles
# Register your models here.
class profile(admin.ModelAdmin):
    list_display=('name','amount_paid','amount_balance')


admin.site.register(profiles,profile)    