from django.contrib import admin

from .models import Myr
from .models import Mysql

admin.site.register(Myr)
admin.site.register(Mysql)
# Register your models here.
