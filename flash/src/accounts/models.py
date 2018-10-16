"""
Author: Andrea Murphy
Last Updated: April 17
Relative File Path: flash/src/accounts/models.py
Description: accounts models for FlashCourse application
Database: FlashCourses- mySQL
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

from courses.models import Institution

import uuid


class UserProfile(models.Model):
    """
    UserProfile model
    Primary Key: Django auto ID
    Foreign Key: User from django.contrib.auth.models
    Foreign Key: Institition from courses.models
    """
    parent_user = models.ForeignKey(
        User,  on_delete=models.CASCADE, default=1
        )
    parent_institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, default=1
        )
