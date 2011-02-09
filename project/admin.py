from django.contrib import admin  
from shiraha.project.models import Project, MemberContribution 

class MemberContributionInline(admin.TabularInline):
    model = MemberContribution 
    extra = 5 
    max_num = 100 
	
class ProjectAdmin (admin.ModelAdmin): 
    list_display = ( 'name', 'type', 'start', 'finish', 'location', 'category', 'description', 'total_cost')
    inlines = [MemberContributionInline,] 
    list_filter = ['type', 'category', 'location'] 
    fields = [ 'name', 'slug', 'type', 'start', 'finish', 'location', 'category', 'total_cost', 'description']  
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}
	
admin.site.register (Project, ProjectAdmin)