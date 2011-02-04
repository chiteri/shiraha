from django.db import models 
from django.contrib.flatpages.models import FlatPage 
from shiraha.core.models import Member 
import datetime 

# Create your models here. 
class News(models.Model): 
    title = models.CharField(max_length=50) 
    submitter = models.ForeignKey(Member) 
    article = models.TextField() 
    pub_date = models.DateTimeField(default=datetime.datetime.now, help_text="Date of publication.")  
    slug = models.SlugField() 

    class Meta: 
        ordering = ["-pub_date"] 
        verbose_name_plural = "News"
		
    def __unicode__(self): 
        return u"%s"%self.title

    def get_absolute_url(self): 
        return "/news/%s/%s/"%( self.pub_date.strftime("%Y/%b/%d").lower(), self.slug )	
