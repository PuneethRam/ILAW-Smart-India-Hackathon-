# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Case(models.Model):
    case_name=models.CharField(max_length=120)
    case_description=models.TextField(max_length=100,default=True)
    case_status=models.CharField(max_length=40,default=True)
    hash_key=models.CharField(max_length=40,default=False)
    transaction_id=models.CharField(max_length=40,default=False)


    def __str__(self):
        return self.case_name

    
class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Sec(models.Model):
    sec_name=models.CharField(max_length=50)
    sec_def=models.TextField(max_length=100,default=True)

    def __str__(self):
        return self.sec_def

class UploadCaseFile(models.Model):
    uploadfile = models.FileField(upload_to='media',null=True,blank=True)
    file_descripion=models.TextField(default='sample')

    def __str__(self):
        return self.file_descripion

        

