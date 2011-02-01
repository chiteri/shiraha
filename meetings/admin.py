from django.contrib import admin 
from shiraha.meetings.models import Meeting, Minutes 

class MinutesInline(admin.TabularInline):
    model = Minutes 
    extra = 1 
    max_num = 2 

class MeetingAdmin (admin.ModelAdmin): 
    list_display = ( 'agenda', 'type', 'host', 'day_held', 'location')
    inlines = [MinutesInline,] 
    list_filter = ['type'] 
    fields = ['host', 'day_held', 'location', 'type', 'agenda', 'slug', 'announcement' ]  
    prepopulated_fields = {"slug": ("agenda",)}
	
    search_fields = ['host'] 
	
admin.site.register (Meeting, MeetingAdmin)