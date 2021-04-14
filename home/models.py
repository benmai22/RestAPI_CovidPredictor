from django.db import models

class covid(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	UNDERLYING_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	ETHENICITY_CHOICES = (
        ('White', ' White'),
		('American Indian', 'American Indian'),
        ('Non-Hispanic', ' Non-Hispanic'),
        ('Alaska Native', ' Alaska Native'),
        ('Native Hawaiian','Native Hawaiian'),
        ('Other Pacific Islander','Other Pacific Islander'),
        ('Hispanic','Hispanic'),
        ('Latino','Latino'),
        ('Black,','Black,'),
        ('Other','Other')
	)
	SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	age=models.IntegerField(default=0)
	gender=models.CharField(max_length=15, choices=GENDER_CHOICES)
	ethnicity=models.CharField(max_length=40, choices=ETHENICITY_CHOICES)
	underlying=models.CharField(max_length=15, choices=UNDERLYING_CHOICES)
	

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)   