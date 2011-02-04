from django.contrib import admin 
from shiraha.news.models import News 

class NewsAdmin(admin.ModelAdmin): 
    list_display = ('title', 'submitter', 'pub_date') 
    list_filter = ['submitter'] 
    fields = ['submitter', 'pub_date', 'title', 'slug', 'article' ] 
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)