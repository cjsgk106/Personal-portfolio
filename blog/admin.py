from django.contrib import admin

from .models import Myr
from .models import Mysql
from .models import Mypy

admin.site.register(Myr)
admin.site.register(Mysql)
admin.site.register(Mypy)
# Register your models here.
