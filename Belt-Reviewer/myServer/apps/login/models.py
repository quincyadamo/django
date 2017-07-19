from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here:
class UserManager(models.Manager):
    def valid_registration(self, user_info, request):
        valid = True
        if not user_info['first_name'].isalpha():
            messages.warning(request, "First name must be all letters!")
            valid = False
        if len(user_info['first_name']) < 2:
            messages.warning(request, "First name must be 2 or more characters long!")
            valid = False
        if not user_info['last_name'].isalpha():
            messages.warning(request, "Last name must be all letters!")
            valid = False
        if len(user_info['last_name']) < 2:
            messages.warning(request, "Last name must be 2 or more characters long!")
            valid = False
        if not EMAIL_REGEX.match(user_info['email_address']):
            messages.warning(request, "Email is not a valid email!")
            valid = False
        if len(user_info['password']) < 7:
            messages.warning(request, "Password is too short!")
            valid = False
        if user_info['password'] != user_info['confirm_password']:
            messages.warning(request, "Passwords do not match!")
            valid = False
        if User.objects.filter(email = user_info['email_address']):
            messages.error(request, "This Email already exists!")
            valid = False
        if valid == True:
            # messages.success(request, "Successful registration, " + user_info['first_name'] + "!")
            hashed = bcrypt.hashpw(user_info['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email_address'], password = hashed)
        return valid

    def exisiting_user(self, user_info, request):
        valid = True
        if User.objects.filter(email = user_info['email_address']):
            hashed = User.objects.get(email = user_info['email_address']).password
            hashed = hashed.encode('utf-8')
            password = user_info['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                # messages.success(request, "Success! Welcome back, " + User.objects.get(email = user_info['email_address']).first_name + "!")
                valid = True
            else:
                messages.warning(request, "Oops! You entered an incorrect password!")
                valid = False
        else:
            messages.warning(request, "Oops! Your email is incorrect!")
            valid = False
        return valid

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UserManager = UserManager()
    objects = models.Manager()
