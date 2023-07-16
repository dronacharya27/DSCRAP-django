from django.contrib import admin
from .models import contact
from .models import Document
from .models import useraddress

admin.site.register(contact)
admin.site.register(Document)
admin.site.register(useraddress)