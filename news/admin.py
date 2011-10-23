from django.contrib import admin 
from shiraha.news.models import News 

class NewsAdmin(admin.ModelAdmin): 
    list_display = ('pub_date', 'article') 
    list_filter = ['pub_date'] 
    fields = ['pub_date', 'article' ] 
    # prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)