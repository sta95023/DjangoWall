from django.db import models

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['user_email']) < 15:
            errors['user_email'] = "Users email MUST be at least 15 characters long"
        if len(postData['user_password']) < 12:
            errors['user_password'] = "Users password MUST be at least 12 characters long"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Messages(models.Model):
    messages = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comments = models.CharField(max_length=500)
    message = models.ForeignKey(Messages, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)