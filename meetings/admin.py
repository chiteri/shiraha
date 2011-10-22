from django.contrib import admin 
from shiraha.meetings.models import Meeting, Minutes 

# class AttendanceInline(admin.TabularInline):
#    model = Attendance 
#    extra = 5 
#    max_num = 50 

class MeetingAdmin (admin.ModelAdmin): 
    list_display = ( 'day_held', 'host', 'location', 'description' )
    # inlines = [AttendanceInline,] 
    # list_filter = ['type'] 
    fields = ['host', 'day_held', 'location', 'slug', 'description' ]  
    prepopulated_fields = {"slug": ("location",)}
    list_filter = ['day_held']
    date_hierarchy = 'day_held'
    search_fields = ['host'] 
	
class MinutesAdmin (admin.ModelAdmin): 
    list_display = ( 'pub_date', 'meeting' )
    fields = ['pub_date', 'meeting', 'content' ]  
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['pub_date'] 
	
admin.site.register (Meeting, MeetingAdmin)
admin.site.register (Minutes, MinutesAdmin)