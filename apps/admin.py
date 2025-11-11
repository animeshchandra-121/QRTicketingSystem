from django.contrib import admin
from .models import MessProfile, MessVisit, OneTimeToken
# Register your models here.

admin.site.register(MessProfile)
admin.site.register(MessVisit)
admin.site.register(OneTimeToken)