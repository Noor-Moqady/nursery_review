from django.db import models
from datetime import datetime
from time import gmtime, strftime
from django.utils import timezone
import re
import bcrypt

class Roles(models.Model):
    roles_name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['parent_name']) < 2:
            errors["parent_name"] = "Parent Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "This email is already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['password']= 'Password not match'
       
        if postData['birthday'] !=''  and (datetime.strptime(postData['birthday'], "%Y-%m-%d")) >= (datetime.now()):
            errors["birthday"] = "Birthday should be in the past"
        return errors


class User(models.Model):
    parent_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.TextField()
    birthday= models.DateTimeField(null=True)
    user_roles = models.ForeignKey(Roles, related_name ='user', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Location(models.Model):
    address = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    governarate = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Nursery(models.Model):
    nursery_name = models.CharField(max_length=225)
    facilities = models.CharField(max_length=225)
    program_offered = models.CharField(max_length=225)
    contact_number = models.IntegerField()
    nursery_location = models.ForeignKey(Location, related_name ='nursery', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Review(models.Model):
    review = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name ='review', on_delete = models.CASCADE)
    nursery_review = models.ForeignKey(Nursery, related_name ='review', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Nursery_section(models.Model):
    section_name = models.CharField(max_length=225)
    childage_min = models.IntegerField()
    childage_max = models.IntegerField()
    nursery_section= models.ManyToManyField(Nursery, related_name='nursery_seciton')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Rating(models.Model):
    rating = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name ='rating', on_delete = models.CASCADE)
    nursery_rating = models.ForeignKey(Nursery, related_name ='rating', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

