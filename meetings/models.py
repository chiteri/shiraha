from django.db import models
# from shiraha.core.models import Member 
from django.contrib.flatpages.models import FlatPage
from markdown import markdown
import datetime 

# Create your models here.
class Meeting(models.Model): 
    # Core fields 
    day_held = models.DateTimeField(default=datetime.datetime.now, help_text="The day the meeting was or will be held.") 
    host = models.CharField(max_length=100)
    location = models.CharField(max_length=200) 
    map = models.URLField(null=True, blank=True, help_text="A map showing the location of the meeting.")
    description = models.TextField(null=True, help_text="Provide the agenda of the meeting and other information important for members.") 

    # Extra fields to store the generated html
    description_html = models.TextField(editable=False, blank=True)

    # Metadata	
    slug = models.SlugField()
	
    class Meta: 
        ordering = ['-day_held'] 
		
    def __unicode__(self): 
        return u"Meeting held on %s at %s"%(self.day_held, self.location) 

    def get_absolute_url(self): 
        return "/meeting/%s/%s/"%(self.day_held.strftime("%Y/%b/%d").lower(), self.slug ) 
		
    def save(self, force_insert=False, force_update=False): 
        self.description_html = markdown(self.description)
        super(Meeting, self).save(force_insert, force_update)

# Minutes for a meeting, superceded by the minutes attribute inside the Meeting model.		
class Minutes(models.Model): 
    pub_date = models.DateField(help_text="The day the minutes were published.") 
    drafted_by = models.CharField(max_length=50) 
    meeting = models.ForeignKey(Meeting, related_name='the_meeting') 
    content = models.TextField() 

    # Extra fields to store the generated html
    content_html = models.TextField(editable=False, blank=True)   
	
    class Meta: 
        ordering = ['-pub_date'] 
        verbose_name_plural = "Minutes" 
		
    def __unicode__(self): 
        return u"Minutes for %s"%self.meeting 
	
    def get_absolute_url(self): 
        return "/meeting/minutes/%s/%s/"%(self.meeting.day_held.strftime("%Y/%b/%d").lower(), self.meeting.slug) 
		
    def save(self, force_insert=False, force_update=False): 
        self.content_html = markdown(self.content)
        super(Minutes, self).save(force_insert, force_update)