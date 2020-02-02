from django.contrib import admin
from . import models

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','status','created_on','updated_on')
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.BlogPost, BlogPostAdmin)