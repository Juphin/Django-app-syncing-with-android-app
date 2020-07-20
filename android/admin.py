from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')
    list_filter = ('title', )


admin.site.register(Publication, PublicationAdmin)