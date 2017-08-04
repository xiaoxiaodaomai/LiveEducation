# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.utils import timezone

class Post(models.Model):
    str = models.CharField(max_length=100)
	
class User(AbstractUser):
	isTeacher = models.BooleanField(default=False)

class Room(models.Model):
	author = models.ForeignKey('backend.User')
	roomName = models.CharField(max_length=100)
	studentNum = models.IntegerField(default=0)
	createTime = models.DateTimeField(default=timezone.now)

class roomStudent(models.Model):
	roomId = models.ForeignKey('backend.Room')
	studentId = models.ForeignKey('backend.User')

class stuBlackList(models.Model):
	roomId = models.ForeignKey('backend.Room')
	studentId = models.ForeignKey('backend.User')
		
=======


class User(AbstractUser):
    isTeacher = models.BooleanField(default=False)
    name = models.CharField(default='', max_length=16)
>>>>>>> b11a7a4777db9e1358d1cdcab558f72bbaa96fde
# Create your models here.
