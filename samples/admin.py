from django.contrib import admin
from .models import CV, Others, Python, Website

#
# class CVAdmin(admin.ModelAdmin):
#     list_display = []


admin.site.register(CV)
admin.site.register(Others)
admin.site.register(Python)
admin.site.register(Website)
