from django.db import models
from shiraha.core.models import Member 
from django.contrib.flatpages.models import FlatPage
import datetime 

# Create your models here.
class Meeting(models.Model): 
    WELFARE = 1 
    INVESTMENT = 2 
    SPOUSE = 3 
    YOUTH = 4 
    OTHER = 5 
    MEETING_TYPE_CHOICES = (
	    (WELFARE, 'Welfare'), 
	    (INVESTMENT, 'Investment'), 
	    (SPOUSE, 'Spouse'), 
	    (YOUTH, 'Youth'),
	    (OTHER, 'Other'),
	) 
	
    # Core fields 
    day_held = models.DateTimeField(default=datetime.datetime.now, help_text="The day the meeting was or will be held.") 
    host = models.ForeignKey(Member, blank=True, null=True, help_text="Which member will host or hosted the meeting.") 
    location = models.CharField(max_length=40) 
    type = models.IntegerField(max_length=1, choices=MEETING_TYPE_CHOICES)
    agenda = models.CharField(max_length=150) 
    announcement = models.TextField(blank=True, null=True) 
    slug = models.SlugField()
    # slug = models.SlugField(prepopulate_from=['agenda'], unique_for_date=day_held, help_text="Suggested value automatically generated from the agenda.") 
	
    class Meta: 
        ordering = ['-day_held'] 
		
    def __unicode__(self): 
        return u"%s meeting held on %s at %s, Agenda: %s."%(self.type, self.day_held, self.location, self.agenda) 

    def get_absolute_url(self): 
        return "/meeting/%s/%s/"%(self.day_held.strftime("%Y/%b/%d").lower(), self.slug ) 
		
class Minutes(models.Model): 
    pub_date = models.DateField(help_text="The day the minutes were published.") 
    drafted_by = models.ForeignKey(Member, blank=True, null=True) 
    meeting = models.ForeignKey(Meeting, related_name='the_meeting') 
    content = models.ForeignKey(FlatPage, unique=True) 
	
    class Meta: 
        ordering = ['-pub_date'] 
        verbose_name_plural = "Minutes" 
		
    def __unicode__(self): 
        return u"Minutes for %s"%self.meeting 
	
    def get_absolute_url(self): 
        return "/minutes/%s/"%self.pub_date.strftime("%Y/%b/%d").lower()