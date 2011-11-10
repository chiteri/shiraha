from django.db import models 
from markdown import markdown 
import datetime 

# Create your models here. 
class News(models.Model): 
    # Core Fields 
    title = models.CharField(max_length=50) 
    pub_date = models.DateTimeField(default=datetime.datetime.now, help_text="Date of publication.")  
    article = models.TextField()

	# Extra field for the storage of generated html 
    article_html = models.TextField(editable=False, blank=True)
	
    # Metadata 
    author = models.CharField(max_length=50) 
    slug = models.SlugField()

    class Meta: 
        ordering = ["-pub_date"] 
        verbose_name_plural = "News"
		
    def __unicode__(self): 
        return u"%s"%self.title

    def get_absolute_url(self): 
        return "/news/%s/%s/"%( self.pub_date.strftime("%Y/%b/%d").lower(), self.slug )	

    def save(self, force_insert=False, force_update=False): 
        self.article_html = markdown(self.article)
        super(News, self).save(force_insert, force_update)