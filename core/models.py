from django.db import models
from django.contrib.auth.models import User 
import datetime 

# Create your models here.
class Member(models.Model): 
    # Sexes 
    GENDER_CHOICES = (
        (u'M', u'Male'), 
        (u'F', u'Female'), 
    )    
    # Marital statuses  
    SINGLE_STATUS = 1 
    MARRIED_STATUS = 2 
    DIVORCED_STATUS = 3 
    WIDOWED_STATUS = 4 
    MARITAL_STATUS_CHOICES = (
        (SINGLE_STATUS, 'Single'), 
        (MARRIED_STATUS, 'Married'), 
        (DIVORCED_STATUS, 'Divorced'), 
        (WIDOWED_STATUS, 'Widowed'), 
    )	
    
    # Core Fields 	
    user = models.ForeignKey(User, unique=True)  
    
    # Personal Information  
    date_of_birth = models.DateField() 
    gender=models.CharField(max_length=2, choices=GENDER_CHOICES) 
    marital_status = models.IntegerField(max_length=2, choices=MARITAL_STATUS_CHOICES) 
    id_or_passport_number = models.CharField(max_length=8, help_text="National ID. or Passport number.")
	
    # Contact Information 
    cellphone_number = models.CharField(max_length=20, unique=True, help_text='Mobile phone number.') 
    telephone_number = models.CharField(blank=True, max_length=20, help_text='Fixed line number, if exists.') 
    postal_address = models.CharField(blank=True, max_length=50)
    physical_address = models.CharField(max_length=50) 	
    residence_area = models.CharField(max_length=30) 
    house_number = models.CharField(blank=True, max_length=20) 
	
    # Membership information 
    admission_date = models.DateField() 
    cessation_date = models.DateField(blank=True, null=True) 
    membership_number = models.CharField(max_length=10, unique=True)
	
    # class Meta: 
    #    abstract = True 
		
    def __unicode__(self): 
        return u"%s's Profile"%(self.user)	
		
class NextOfKin(models.Model): 
    # Next of kin relationships   
    FATHER = 1 
    MOTHER = 2 
    BROTHER = 3 
    SISTER = 4 
    GRAND_FATHER = 5 
    GRAND_MOTHER = 6
    COUSIN = 7 
    HUSBAND = 8 
    WIFE = 9 
    SON = 10 
    DAUGHTER = 11 
    NIECE = 12 
    NEPHEW = 13 
    AUNT = 14 
    UNCLE = 15 
    FRIEND = 16
    OTHER = 17 
    RELATIONS_CHOICES = (
        (FATHER, 'Father'), 
        (MOTHER, 'Mother'), 
        (BROTHER, 'Brother'), 
        (SISTER, 'Sister'), 
        (GRAND_FATHER, 'Grandfather'), 
        (GRAND_MOTHER, 'Grandmother'), 
        (COUSIN, 'Cousin'), 
        (HUSBAND, 'Husband'), 
        (WIFE, 'Wife'), 
        (SON, 'Son'), 
        (DAUGHTER, 'Daughter'), 
        (NIECE, 'Niece'), 
        (NEPHEW, 'Nephew'), 
        (AUNT, 'Aunt'), 
        (UNCLE, 'Uncle'), 
        (FRIEND, 'Friend'), 
        (OTHER, 'Other'), 
    ) 

    # Core Fields 
    first_names = models.CharField( max_length=40 ) 
    surname = models.CharField(blank=False, max_length=20) 
    relationship = models.IntegerField(blank=False, max_length=2, choices=RELATIONS_CHOICES) 
    telephone_number = models.CharField(blank=True, max_length=20, help_text='Fixed line number, if exists.') 
    cellphone_number = models.CharField(blank=True, max_length=20, help_text='Mobile phone number.') 
    postal_address = models.CharField(blank=True, max_length=50) 
    id_or_passport_number = models.CharField(max_length=8, help_text="National ID. or Passport number.") 
    member = models.ForeignKey(Member, unique=True) # One next of kin per Member
	
    def __unicode__(self): 
        return u"%s %s"%(self.first_names, self.surname)
    