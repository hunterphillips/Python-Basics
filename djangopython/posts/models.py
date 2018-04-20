# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Posts(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  # shows 'title' of posts
  def __str__(self):
    return self.title

  # avoids double 's'
  class Meta:  # model names are auto. made plural when rendered
    verbose_name_plural = "Posts"
