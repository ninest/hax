from django.contrib import admin
from .models import Hack, Tag

admin.site.register(Tag)
admin.site.register(Hack)