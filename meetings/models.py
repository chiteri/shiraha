from django.db import models
# from shiraha.core.models import Member 
from django.contrib.flatpages.models import FlatPage
import datetime 

# Create your models here.
class Meeting(models.Model): 
    # Core fields 
    day_held = models.DateTimeField(default=datetime.datetime.now, help_text="The day the meeting was or will be held.") 
    # host = models.ForeignKey(Member, blank=True, null=True, help_text="Which member will host or hosted the meeting.") 
    host = models.CharField(max_length=100)
    location = models.CharField(max_length=200) 
    map = models.URLField(null=True, blank=True, help_text="A map showing the location of the meeting.")
    description = models.TextField(null=True, help_text="Provide the agenda of the meeting and other information important for members.") 
    # announcement = models.TextField(blank=True, null=True) 
    slug = models.SlugField()
    minutes = models.ForeignKey(FlatPage, null=True, blank=True)
    # slug = models.SlugField(prepopulate_from=['agenda'], unique_for_date=day_held, help_text="Suggested value automatically generated from the agenda.") 
	
    class Meta: 
        ordering = ['-day_held'] 
		
    def __unicode__(self): 
        return u"Meeting held on %s at %s"%(self.day_held, self.location) 

    def get_absolute_url(self): 
        return "/meeting/%s/%s/"%(self.day_held.strftime("%Y/%b/%d").lower(), self.slug ) 

# Minutes for a meeting, superceded by the minutes attribute inside the Meeting model.		
# class Minutes(models.Model): 
#    pub_date = models.DateField(help_text="The day the minutes were published.") 
    # drafted_by = models.ForeignKey(Member, blank=True, null=True) 
#    meeting = models.ForeignKey(Meeting, related_name='the_meeting') 
#    content = models.ForeignKey(FlatPage, unique=True) 
	
#   class Meta: 
#        ordering = ['-pub_date'] 
#        verbose_name_plural = "Minutes" 
		
#    def __unicode__(self): 
#        return u"Minutes for %s"%self.meeting 
	
#    def get_absolute_url(self): 
#        return "/meeting/minutes/%s/"%self.pub_date.strftime("%Y/%b/%d").lower() 