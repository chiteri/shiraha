from django.db import models 
import datetime 
		
# Create your models here.
class Project(models.Model): 
	# Core Fields 
    name = models.CharField(max_length=50, unique=True) 
    description = models.TextField() 
    location = models.CharField(max_length = 30) 
    total_cost = models.IntegerField(null=True, blank=True, help_text="Approximate cost of the project.")
    slug = models.SlugField() 
	
    class Meta:
        ordering = ["-name"]
	
    def __unicode__(self): 
        return u"%s"%self.name 
		
    def get_absolute_url(self): 
        return "/project/%s/"%self.slug 