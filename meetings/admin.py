from django.contrib import admin 
from shiraha.meetings.models import Meeting, Minutes 

class MeetingAdmin (admin.ModelAdmin): 
    list_display = ( 'day_held', 'host', 'location', 'map' )
    # inlines = [AttendanceInline,] 
    # list_filter = ['type'] 
    fields = ['host', 'day_held', 'location', 'map', 'slug', 'description' ]  
    prepopulated_fields = {"slug": ("location",)}
    list_filter = ['day_held']
    date_hierarchy = 'day_held'
    search_fields = ['host'] 
	
class MinutesAdmin (admin.ModelAdmin): 
    list_display = ( 'drafted_by', 'pub_date', 'meeting' )
    fields = ['drafted_by', 'pub_date', 'meeting', 'content' ]  
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['pub_date'] 
	
admin.site.register (Meeting, MeetingAdmin)
admin.site.register (Minutes, MinutesAdmin)