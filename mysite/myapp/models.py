from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-

class Students(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        ordering = ('name','password','email',)


