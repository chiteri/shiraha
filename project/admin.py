from django.contrib import admin  
from shiraha.project.models import Project

class ProjectAdmin (admin.ModelAdmin): 
    list_display = ( 'name', 'location', 'description', 'total_cost')
    list_filter = ['location'] 
    fields = [ 'name', 'slug', 'location', 'map', 'description', 'total_cost']  
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
	
admin.site.register (Project, ProjectAdmin)