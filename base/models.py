from django.db import models

# Create your models here.

class Common(models.Model):
	name=models.CharField(max_length=100)
class StudentType(Common):
	pass
class GuideCategory(Common):
	pass
class Department(Common):
	pass
class SocialCategory(Common):
	pass
class Program(Common):
	pass
class Qualification(Common):
	pass
class Contact(models.Model):
	name=models.CharField(max_length=30)
        phone_no=models.CharField(max_length=15)
        email=models.CharField(max_length=30)
	address=models.CharField(max_length=150)

class Guide(models.Model):
        name=models.CharField(max_length=30)
        contact=models.ForeignKey(Contact)
        category=models.ForeignKey(GuideCategory)
        department=models.ForeignKey(Department)

class Student(models.Model):
	name=models.CharField(max_length=30)
        hall_ticket_no=models.CharField(max_length=15)
        admn_no=models.CharField(max_length=15)
	reg_no=models.CharField(max_length=15)	
        category=models.ForeignKey(SocialCategory)
        program=models.ForeignKey(Program)
        sex=models.CharField(max_length=10)
        sub=models.ForeignKey(Department, related_name = "subject")
	father_name=models.CharField(max_length=50)
	guide=models.ForeignKey(Guide, related_name = "guide")
	co_guide=models.ForeignKey(Guide, related_name = "co_guide")
        date_of_birth=models.DateTimeField('date of birth')
        nationality=models.CharField(max_length=50)
	religion=models.CharField(max_length=50)
	present_contact=models.ForeignKey(Contact, related_name = "present_contact")
	original_contact=models.ForeignKey(Contact, related_name = "original_contact")
	department=models.ForeignKey(Department, related_name = "dept_of_spec")
	area_of_specialition=models.CharField(max_length=100)
	date_of_admission=models.CharField(max_length=15)
	stype=models.ForeignKey(StudentType)
	qual1=models.ForeignKey(Qualification, related_name = "qualification_1")
	qual2=models.ForeignKey(Qualification, related_name = "qualification_2")
	