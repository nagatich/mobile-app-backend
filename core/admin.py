from django.contrib import admin

from .models import *

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Generation)
admin.site.register(Modification)
admin.site.register(QueryResult)
