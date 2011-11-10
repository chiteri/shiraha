from django.contrib import admin 
from shiraha.news.models import News 

class NewsAdmin(admin.ModelAdmin): 
    list_display = ('title', 'author', 'pub_date') 
    list_filter = ['pub_date', 'author'] 
    fields = ['title', 'slug', 'author', 'pub_date', 'article' ] 
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)