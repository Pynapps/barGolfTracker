from django.contrib import admin

from .models import Golfer
from .models import BarPar

# Register your models here.
admin.site.register(Golfer)
admin.site.register(BarPar)
