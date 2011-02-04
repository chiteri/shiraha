from django.contrib import admin 
from shiraha.core.models import Member, NextOfKin  
from django.contrib.auth.models import User 

class NextOfKinInline(admin.TabularInline):
    model = NextOfKin 
    fk_name = 'member'
    extra = 3 
    max_num = 4 
	
class MemberInline(admin.StackedInline):
    model = Member
    fk_name = 'user'
    max_num = 1 
    # inlines = [NextOfKinInline,] 
    fieldsets = [
        ('Personal Information', {'fields': ['date_of_birth', ('gender', 'marital_status'), 'id_or_passport_number'], 'classes': [ 'extrapretty']}), 
        ('Contact Information', {'fields': ['cellphone_number', 'telephone_number', 'postal_address', ('physical_address', 'house_number'),
		'residence_area' ], 'classes': [ 'extrapretty'] } ), 
        ('Membership Information', {'fields': ['membership_number', 'admission_date', 'cessation_date'], 'classes': [ 'extrapretty']}), 
    ] 
	
class MemberAdmin(admin.ModelAdmin):
    list_display=('user', 'membership_number', 'marital_status', 'admission_date', 'cessation_date', 'residence_area')
    inlines = [NextOfKinInline,] 
    list_filter = ['marital_status'] 
    fieldsets = [('User Information', {'fields': ['user'], 'classes': [ 'extrapretty']}),
        ('Personal Information', {'fields': ['date_of_birth', ('gender', 'marital_status'), 'id_or_passport_number'], 'classes': [ 'extrapretty']}), 
		('Contact Information', {'fields': ['cellphone_number', 'telephone_number', 'postal_address', ('physical_address', 'house_number'),
		'residence_area' ], 'classes': [ 'extrapretty'] } ),  
        ('Membership Information', {'fields': ['membership_number', 'admission_date', 'cessation_date'], 'classes': [ 'extrapretty']}),
    ] 
    search_fields  = ['membership_number', 'id_or_passport_number']	

class NewMemberAdmin(admin.ModelAdmin):
    inlines = [MemberInline, ]		
	
# admin.site.unregister(User) 
# admin.site.register(User, NewMemberAdmin) 
admin.site.register(Member, MemberAdmin)