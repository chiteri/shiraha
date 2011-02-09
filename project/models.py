from django.db import models 
from shiraha.core.models import Member 
import datetime 

class InvestmentManager(models.Manager): 
    def get_query_set(self): 
        return super(InvestmentManager, self).get_query_set().filter(type=Project.INVESTMENT) 

		
class WelfareProjectManager(models.Manager): 
    def get_query_set(self): 
        return super(WelfareProjectManager, self).get_query_set().filter(type=Project.WELFARE) 
		
# Create your models here.
class Project(models.Model): 
    WELFARE = 1 
    INVESTMENT = 2 
    PROJECT_TYPE_CHOICES = ( 
        (WELFARE, 'Welfare'), 
        (INVESTMENT, 'Investment'), 		
	)
	
    CHURCH = 1 
    EDUCATION = 2 
    SPORTS = 3  
    FARMING = 4 
    CONSTRUCTION = 5	
    REAL_ESTATE = 6 
    STOCK_MARKET = 7  
    PROJECT_CATEGORY_CHOICES = (
	    (CHURCH, 'Church'), 
	    (EDUCATION, 'Education'), 
	    (SPORTS, 'Sports'), 
	    (FARMING, 'Farming'), 
	    (CONSTRUCTION, 'Construction'), 
	    (REAL_ESTATE, 'Real Estate'), 
	    (STOCK_MARKET, 'Stock Market'),  
	)
	
	# Core Fields 
    name = models.CharField(max_length=50, unique=True) 
    description = models.TextField() 
    type = models.IntegerField(choices=PROJECT_TYPE_CHOICES) 
    location = models.CharField(max_length = 30) 
    total_cost = models.IntegerField(null=True, blank=True)
    start = models.DateField() 
    finish = models.DateField() 
    category = models.IntegerField(choices=PROJECT_CATEGORY_CHOICES) 
    objects = models.Manager() # The default manager.
    welfare = WelfareProjectManager() # The manager for all the welfare's projects
    investments = InvestmentManager() # A manager for the projects geared towards making profits 
    slug = models.SlugField() 
	
    class Meta:
        ordering = ["-start"]
	
    def __unicode__(self): 
        return u"%s"%self.name 
		
    def get_absolute_url(self): 
        if self.type == self.INVESTMENT: 
            return "/investment/%s/"%self.slug
        return "/project/%s/"%self.slug 
				
class Contribution(models.Model): 
    submission_date = models.DateField() 
    amount = models.IntegerField() 
    project = models.ForeignKey(Project, related_name='the_project')  
	
    class Meta: 
        ordering = ["-submission_date"] 
	
class MemberContribution(Contribution): 
    member = models.ForeignKey(Member, related_name='giver')