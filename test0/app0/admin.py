from django.contrib import admin
from .models import UserMetaInfo, PaperMetaInfo

# Register your models here.


class QustionAdmin(admin.ModelAdmin):
    fields = ['name', 'id']

admin.site.register(UserMetaInfo, QustionAdmin)
admin.site.register(PaperMetaInfo)


