from django.contrib import admin 
from shiraha.meetings.models import Meeting, Attendance 

class AttendanceInline(admin.TabularInline):
    model = Attendance 
    extra = 5 
    max_num = 50 

class MeetingAdmin (admin.ModelAdmin): 
    list_display = ( 'agenda', 'type', 'host', 'day_held', 'location')
    inlines = [AttendanceInline,] 
    list_filter = ['type'] 
    fields = ['host', 'day_held', 'location', 'type', 'agenda', 'slug', 'announcement', 'minutes' ]  
    prepopulated_fields = {"slug": ("agenda",)}
	
    search_fields = ['host'] 
	
admin.site.register (Meeting, MeetingAdmin)