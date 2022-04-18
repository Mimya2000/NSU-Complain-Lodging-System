from django.contrib import admin
from .models import Complaints, Comments, History

admin.site.register(Complaints)
admin.site.register(Comments)
admin.site.register(History)
