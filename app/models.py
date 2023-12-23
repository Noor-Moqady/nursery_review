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

class Facilities(models.Model):
    facilities_name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Programs(models.Model):
    program_offered_name = models.CharField(max_length=225)
    childage_min = models.IntegerField(null=True)
    childage_max = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NurseryManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['nursery_name']) < 5:
            errors["nursery_name"] = "Nursery Name should be at least 5 characters"
        if User.objects.filter(email=postData['nursery_name']).exists():
            errors["nursery_name"] = "This nursery is already exists"
        
        return errors

class Nursery(models.Model):
    nursery_name = models.CharField(max_length=225)
    facilities = models.ManyToManyField(Facilities, related_name='nursery')
    program_offered = models.ManyToManyField(Programs, related_name='nursery')
    contact_number = models.CharField(max_length=225)
    nursery_location = models.TextField(null = True)
    image= models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NurseryManager()

class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['review']) < 15:
            errors["review"] = "Review should be at least 15 characters" 
        return errors

class Review(models.Model):
    review = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name ='review', on_delete = models.CASCADE)
    nursery_review = models.ForeignKey(Nursery, related_name ='review', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()


