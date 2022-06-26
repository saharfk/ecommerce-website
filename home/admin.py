from django.contrib import admin
from .models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['service', 'comment']


admin.site.register(Comments)
