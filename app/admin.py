from django.contrib import admin
from app import models


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Author)
