from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters"
        if len(postData['description']) != 0 and len(postData['description']) < 15:
            errors["description"] = "Course description should be at least 15 characters"
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["comment"]) < 1:
            errors["comment"] = "Course comment should not be empty"
        return errors

class Description(models.Model):
    content = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Description)   # add one to one relationship
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):          # add course-comment one-to-many relationship
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")
    objects = CommentManager()
