"""
Author: Andrea Murphy
Last Updated: April 17
Relative File Path: flash/src/courses/models.py
Description: course models for FlashCourse application
Database: FlashCourses- mySQL
"""
from django.db import models
import uuid

class Institution(models.Model):
    """
    Institution model
    Primary Key: Django auto ID
    """
    ipeds = models.CharField(
                                max_length=64,
                                null=False,
                                blank=False)
    institution_name = models.CharField(
                                max_length=64,
                                null=False,
                                blank=False)
    location = models.CharField(
                                max_length=64,
                                null=False,
                                blank=False)
    unique_id = models.UUIDField(
                                default=uuid.uuid4,
                                editable= False,
                                unique=True)

    def __str__(self):
        return self.institution_name + ' , ' + self.location


class Course(models.Model):
    """
    Course model
    Primary Key: Django auto ID
    Foreign Key: Institition from courses.models
    """
    course_title = models.CharField(
                                max_length=64,
                                null=False,
                                blank=False)
    course_id = models.CharField(
                                max_length=64,
                                null=False,
                                blank=False)
    parent_institution = models.ForeignKey(
                                Institution,
                                on_delete=models.CASCADE,
                                default=1)
    course_description = models.CharField(
                                max_length=64,
                                null=False,
                                blank=True)
    unique_id = models.UUIDField(
                                default=uuid.uuid4,
                                editable= False,
                                unique=True)

    def __str__(self):
        return self.course_title + ' , ' + self.course_id
