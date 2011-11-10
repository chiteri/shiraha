from django.db import models 
from markdown import markdown 
import datetime 
		
# Create your models here.
class Project(models.Model): 
	# Core Fields 
    name = models.CharField(max_length=50, unique=True) 
    description = models.TextField() 
    location = models.CharField(max_length = 30) 
    map = models.URLField(null=True, blank=True, help_text="A map showing the actual location of the project.")
    total_cost = models.IntegerField(null=True, blank=True, help_text="Approximate cost of the project.")
    slug = models.SlugField()

    # Extra field for the storage of generated html 
    description_html = models.TextField(editable=False, blank=True)	
	
    class Meta:
        ordering = ["-name"]
	
    def __unicode__(self): 
        return u"%s"%self.name 
		
    def get_absolute_url(self): 
        return "/project/%s/"%self.slug 
		
    def save(self, force_insert=False, force_update=False): 
        self.description_html = markdown(self.description)
        super(Project, self).save(force_insert, force_update)